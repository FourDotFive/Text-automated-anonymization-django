from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class FileUploadForm(forms.Form):
    file = forms.FileField()


class TextUploadForm(forms.Form):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Add Bootstrap class for styling
            # 'rows': 8,
            'rows': 12,
            'placeholder': 'Enter your text here...',
            'maxlength': 1024
        })
    )

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('Text must be at least 10 characters long.')
        elif len(text) > 1024:
            raise forms.ValidationError('Text must be shorter than 512 characters.')
        return text


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username'
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
        return cleaned_data


class TextRequestForm(forms.Form):
    redacted_text = forms.CharField(max_length=1024)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        help_text='<ul><li>Minimum length is 5 characters, maximum is 32.</li>'
                  '<li>Can only contain letters, numbers, dashes and underscores.</li></ul>'
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text='<ul><li>Your password can’t be too similar to your other personal information.</li>'
                  '<li>Your password must contain at least 8 characters.</li></ul>'
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        help_text='Enter the same password as before, for verification.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise ValidationError('Nickname is too short')
        user = User.objects.filter(username=username)
        if user.count():
            raise ValidationError('User {} already exists'.format(username))
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('Passwords should have a minimum of 8 characters.')
        if len(password1) > 64:
            raise ValidationError('The maximum length of a password is 64 characters.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise ValidationError('The password and confirm password fields do not match')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )
        return user
