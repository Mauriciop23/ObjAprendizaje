from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Objetivos.models import Objeto, Usuario
from django.http.response import HttpResponse, HttpResponseRedirect
from Objetivos.forms import ObjetoForm
import datetime

@login_required
def home(request):
    if request.user.rol == 'alumno': profesor = False
    else: profesor = True
    context = {
        'nombre_usuario': request.user.nombres,
        'apellidos_usuario': request.user.apellidos,
        'profesor': profesor
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
            'nombre_usuario': request.user.nombres,
            'activo_general': "active"
        }
        if request.method == "POST":
            if "addobjeto" in request.POST:
                objeto = request.POST.copy()
                objeto['autor_principal']=request.user.username
                objeto['estatus']='activo'
                objeto['fecha']=datetime.datetime.now()
                form = ObjetoForm(objeto)
                if form.is_valid():
                    objeto_guardado = form.save()
                    idobjeto = objeto_guardado.idobjeto
                    objeto2 = Objeto.objects.get(pk=idobjeto)
                    documentos = ObjetoForm(objeto, request.FILES, instance=objeto2)
                    documentos.save()
                    return HttpResponseRedirect('/dashboard/')
                else:
                    print("Invalido")
        return render(request, 'dashboard_general.html', context)

def dashboardContenido(request):
    context = {
            'nombre_usuario': request.user.nombres,
            'activo_contenido': "active"
        }
    return render(request, 'dashboard_contenido.html', context)

def objeto(request):
    return render(request, 'objeto.html')
