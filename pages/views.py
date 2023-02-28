
from urllib.request import Request
from django.shortcuts import render


def Home(request):
    return render(request, 'pages/home.html')


def About(request):
    return render(request, 'pages/about.html')


def Services(request):
    return render(request, 'pages/services.html')


def Contact(request):
    return render(request, 'pages/contact.html') 