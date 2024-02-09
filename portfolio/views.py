from django.shortcuts import render
from django.utils import timezone
from .models import Projects
from django.conf import settings
import os

def home(request):
    werken = Projects.objects.all().order_by('-id')[0:4]
    link = "/media/"
    
    return render(request, 'portfolio/home.html', {'werken': werken, 'link': link})

def contact(request):
    return render(request, 'portfolio/contact.html')

def mijn_werk(request):
    werken = Projects.objects.order_by('id')
    link = "/media/"
    return render(request, 'portfolio/mijn_werk.html', {'werken': werken, 'link': link})

def over_mij(request):
    return render(request, 'portfolio/over_mij.html')

def services(request):
    return render(request, 'portfolio/services.html')