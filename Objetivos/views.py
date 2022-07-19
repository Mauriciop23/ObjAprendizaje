from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Objetivos.models import objeto, Usuario
from django.http.response import HttpResponse, HttpResponseRedirect
from Objetivos.forms import ObjetoForm

@login_required
def home(request):
    context = {
        'nombre_usuario': request.user.nombres,
        'apellidos_usuario': request.user.apellidos
    }
    return render(request, 'index.html', context)

def registro(request):
    return render(request, 'register.html')

@login_required
def dashboardGeneral(request):
    if request.user.rol == 'alumno': 
        return HttpResponseRedirect("/home/")
    else:    
        context = {
            'nombre_usuario': request.user.nombres
        }
        if request.method == "POST":
            if "addobjeto" in request.POST:
                objeto = request.POST.copy()
                objeto['estatus']='activo'
                form = ObjetoForm(objeto, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/dashboard/')
                else:
                    print("Invalido")
        return render(request, 'dashboard_general.html', context)

def dashboardContenido(request):
    return render(request, 'dashboard_contenido.html')

def objeto(request):
    return render(request, 'objeto.html')
