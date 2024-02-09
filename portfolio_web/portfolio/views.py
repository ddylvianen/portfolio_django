from django.shortcuts import render
from django.utils import timezone
from .models import Projects
from django.conf import settings
import os

def home(request):
    werken = Projects.objects.order_by('id')[0:4]
    print()
    print()
    print(werken)
    print()
    print()
    link = "/media/"
    
    return render(request, 'portfolio/home.html', {'werken': werken, 'link': link})

def contact(request):
    return render(request, 'portfolio/contact.html')

def mijn_werk(request):
    return render(request, 'portfolio/mijn_werk.html', {'Projects': Projects})

def over_mij(request):
    return render(request, 'portfolio/over_mij.html')

def services(request):
    return render(request, 'portfolio/services.html')