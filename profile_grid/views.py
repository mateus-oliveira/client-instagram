from django.shortcuts import render, redirect
from .services import user_service
from .entity.user import User
from .forms import UserForm

import requests


def login(request):
    if request.method == 'POST': 
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            username = form_user.cleaned_data["username"]
            return redirect('images', username=username)
    else:
        form_user = UserForm()
    
    return render(
        request, 
        'login.html', 
        {
            "form_user": form_user, 
            "title": 'Login com Instagram',
        }
    )

def images(request, username):
    user = user_service.find_user_by_username(username)
    fields='id,media_type,media_url,username,timestamp,caption'
    
    response = requests.get('https://graph.instagram.com/me/media?fields={}&access_token={}'.format(fields, user.token))
    response = response.json()
    return render(request, 'photos/images.html', {
        'user': user, 
        'data': response['data'], 
        'paging': response["paging"],
    })

def videos(request, username):
    user = user_service.find_user_by_username(username)
    fields='id,media_type,media_url,username,timestamp,caption'

    response = requests.get('https://graph.instagram.com/me/media?fields={}&access_token={}'.format(fields, user.token))
    response = response.json()
    return render(request, 'photos/videos.html', {
        'user': user, 
        'data': response['data'], 
        'paging': response["paging"],
    })
