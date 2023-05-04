from django import forms


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


class TextRequestForm(forms.Form):
    redacted_text = forms.CharField(max_length=1024)
