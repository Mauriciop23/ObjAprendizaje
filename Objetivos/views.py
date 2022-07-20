from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Objetivos.models import Objeto, Usuario
from django.http.response import HttpResponse, HttpResponseRedirect
from Objetivos.forms import ObjetoForm
import datetime
from django.contrib import messages

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
    if request.method == "POST" and "addalumno" in request.POST:
        usuario = request.POST.get('registro_Username','')
        contra = request.POST.get('registro_Contraseña','')  
        nombre = request.POST.get('registro_Nombre','')
        apellido = request.POST.get('registro_Apellido','')
        correo = request.POST.get('registro_Correo','')   
        estado = request.POST.get('registro_Estado','')
        institucion = request.POST.get('registro_Institucion','')
        carrera = request.POST.get('registro_Carrera','')
        semestre = request.POST.get('registro_Semestre','')
        telefono = request.POST.get('registro_Telefono','')
        existecorreo = Usuario.objects.filter(email = correo ).exists()
        existeusuario = Usuario.objects.filter(username = usuario ).exists()
        if existecorreo==True or existeusuario==True:
            if existecorreo and existeusuario:
                usm = Usuario.objects.get(username = usuario)
                state = getattr(usm, 'usuario_activo')
                if state == True:
                    messages.error(request, "Ya existe un usuario con el correo y el nombre de usuario ingresados, el usuario no se registró")
                else:
                    usm.set_password(contra)
                    usm.username(usuario)
                    usm.email(correo)
                    usm.nombres(nombre)
                    usm.apellidos(apellido)
                    usm.usuario_activo = True
                    usm.telefono(telefono)
                    usm.institucion(institucion)
                    usm.estado(estado)
                    usm.carrera(carrera)
                    usm.semestre(semestre)
                    usm.save()    
                    messages.success(request, "El usuario se registró con exito")
            if existecorreo and existeusuario==False:
                messages.error(request, "Ya existe un usuario con el correo ingresado, el usuario no se registró")
            if existeusuario and existecorreo==False:
                usm = Usuario.objects.get(username = usuario)
                state = getattr(usm, 'usuario_activo')
                if state == True:
                    messages.error(request, "Ya existe un usuario con el nombre de usuario ingresado, el usuario no se registró")
                else:
                    usm.set_password(contra)
                    usm.username(usuario)
                    usm.email(correo)
                    usm.nombres(nombre)
                    usm.apellidos(apellido)
                    usm.usuario_activo = True
                    usm.telefono(telefono)
                    usm.institucion(institucion)
                    usm.estado(estado)
                    usm.carrera(carrera)
                    usm.semestre(semestre)
                    usm.save()   
                    messages.success(request, "El usuario se registró con exito")
        else:
            usm = Usuario.objects.create_alumno_user(correo,usuario,nombre,apellido,contra,telefono,institucion,estado,carrera,semestre)   
            usm.save()
            messages.success(request, "El usuario se registró con exito")
            return HttpResponseRedirect("/")    
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

def dashboardAdmin(request):
    return render(request, 'dashboard_admin.html')

def objeto(request):
    return render(request, 'objeto.html')
