from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import FileUploadForm, TextUploadForm, LoginForm, TextRequestForm
from .models import TextRecords

from .audio_handler import get_text_from_audio
from .bert_model import anonymize_text

from django_ratelimit.decorators import ratelimit

from langdetect import detect

import json


@ratelimit(key='user', rate='50/d', method='POST', block=False)
@login_required(login_url='/login')
def main_page_view(request):
    if request.method == 'POST':

        if not request.user.is_superuser:  # Don't limit if the user is a superuser
            was_blocked = getattr(request, 'limited', False)
            if was_blocked and request.method == 'POST':
                return render(request, 'request_limit_reached.html')

        audio_form = FileUploadForm(request.POST, request.FILES)
        text_form = TextUploadForm(request.POST)

        # Audio form
        if audio_form.is_valid():
            audio_file = request.FILES['file']
            text = get_text_from_audio(audio_file)

            print(detect(text))

            tokens = anonymize_text(text)
            context = {
                'audio_form': audio_form,
                'text_form': text_form,
                'text': text,
                'tokens': json.dumps(tokens)
            }
            return render(request, 'main.html', context=context)

        # Text form
        if text_form.is_valid():
            text = text_form.cleaned_data['text']

            print(detect(text))

            tokens = anonymize_text(text)
            print(tokens)

            print(tokens)
            context = {
                'audio_form': audio_form,
                'text_form': text_form,
                'text': text,
                'tokens': json.dumps(tokens)
            }
            return render(request, 'main.html', context=context)
        else:
            context = {
                'audio_form': audio_form,
                'text_form': text_form
            }
            return render(request, 'main.html', context=context)
    audio_form = FileUploadForm(request.POST, request.FILES)
    text_form = TextUploadForm(request.POST)
    return render(request, 'main.html', context={'audio_form': audio_form, 'text_form': text_form})


@csrf_exempt
@login_required
def save_record_view(request):
    if request.method == 'POST':
        form = TextRequestForm(request.POST)
        if form.is_valid():
            redacted_text = form.cleaned_data['redacted_text']
            text_request = TextRecords(user=request.user, redacted_text=redacted_text)
            text_request.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})
    else:
        return JsonResponse({'status': 'error'})


@login_required(login_url='/login')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return render(request, 'login.html', context={'login_form': form})
    form = LoginForm()
    return render(request, 'login.html', context={'login_form': form})


@login_required(login_url='/login')
def account_view(request):
    all_records = TextRecords.objects.filter(user=request.user)
    return render(request, 'account.html', context={'all_records': list(all_records), 'test': 'Hello Andrej'})


@login_required(login_url='/login')
def delete_view(request, record_id):
    TextRecords.objects.filter(user=request.user, id=record_id).delete()
    all_records = TextRecords.objects.filter(user=request.user)
    return render(request, 'account.html', context={'all_records': list(all_records)})
