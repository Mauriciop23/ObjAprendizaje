from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'register.html')

def dashboardGeneral(request):
    return render(request, 'dashboard_general.html')

def dashboardContenido(request):
    return render(request, 'dashboard_contenido.html')

def objeto(request):
    return render(request, 'objeto.html')
