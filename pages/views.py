
from urllib.request import Request
from django.shortcuts import render
from .models import Team

def Home(request):
    teams=Team.objects.all()
    data={ 'teams' : teams, }
    return render(request, 'pages/home.html', data)


def About(request):
    teams=Team.objects.all()
    data={ 'teams' : teams, }
    return render(request, 'pages/about.html', data)


def Services(request):
    return render(request, 'pages/services.html')


def Contact(request):
    return render(request, 'pages/contact.html') 