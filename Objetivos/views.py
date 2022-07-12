from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'register.html')
