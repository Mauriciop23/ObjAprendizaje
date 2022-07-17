from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Objetivos.models import objeto
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'register.html')

@login_required
def dashboardGeneral(request):
    return render(request, 'dashboard_general.html')

def dashboardContenido(request):
    return render(request, 'dashboard_contenido.html')

def objeto(request):
    return render(request, 'objeto.html')
