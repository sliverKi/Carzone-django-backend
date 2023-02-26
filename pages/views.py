
from urllib.request import Request
from django.shortcuts import render


def Home(request):
    return render(request, 'pages/home.html');