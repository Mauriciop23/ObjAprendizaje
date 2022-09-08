from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Objetivos.models import Objeto, Usuario, Area, AreaList, DepartamentoList
from django.http.response import HttpResponse, HttpResponseRedirect
from Objetivos.forms import ObjetoForm, AreaForm
import datetime
from django.contrib import messages

@login_required
def home(request):
    if request.user.rol == 'alumno': profesor = False
    else: profesor = True
    objetos = Objeto.objects.filter(estatus = 'activo')
    context = {
        'nombre_usuario': request.user.nombres,
        'apellidos_usuario': request.user.apellidos,
        'profesor': profesor,
        'objetos': objetos
    }
    if request.method == "POST" and "detalles" in request.POST:
        request.session['idobjeto'] = request.POST.get('detalles','')
        return HttpResponseRedirect("/objeto/") 
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
    elif request.user.rol == 'admin':  
        return HttpResponseRedirect("/dashboard_admin/")
    else:       
        context = {
            'nombre_usuario': request.user.nombres,
            'activo_general': "active"
        }
        return render(request, 'dashboard_general.html', context)

@login_required
def dashboardContenido(request):
    objetos = Objeto.objects.filter(autor_principal = request.user.username)
    areas = AreaList.objects.filter(activo = True)
    departamentos = DepartamentoList.objects.filter(activo = True)
    context = {
        'nombre_usuario': request.user.nombres,
        'activo_contenido': "active",
        'objetos': objetos,
        'areas': areas,
        'departamentos': departamentos
    }
    if request.method == "POST":
            if "addobjeto" in request.POST:
                print(request.POST.get('coautores',''))
                objeto = request.POST.copy()
                objeto['autor_principal']=request.user.username
                objeto['autor_principal_nombre']=str(request.user.nombres) + ' ' + str(request.user.apellidos)
                objeto['estatus']='activo'
                objeto['fecha']=datetime.datetime.now()
                objeto['calificacionfinal']=10
                objeto['descargas']=0
                form = ObjetoForm(objeto)
                if form.is_valid():
                    objeto_guardado = form.save()
                    idobjeto = objeto_guardado.idobjeto
                    objeto2 = Objeto.objects.get(pk=idobjeto)
                    documentos = ObjetoForm(objeto, request.FILES, instance=objeto2)
                    documentos.save()
                    if str(request.POST.get('Ciencias Físico Matemáticas','')) == 'Ciencias Físico Matemáticas':
                        Area.objects.create(idobjeto=idobjeto, nombre='Ciencias Físico Matemáticas')
                    if str(request.POST.get('Económico Administrativo','')) == 'Económico Administrativo':
                        Area.objects.create(idobjeto=idobjeto, nombre='Económico Administrativo')
                    if str(request.POST.get('Educación','')) == 'Educación':
                        Area.objects.create(idobjeto=idobjeto, nombre='Educación')
                    if str(request.POST.get('Ingenierías','')) == 'Ingenierías':
                        Area.objects.create(idobjeto=idobjeto, nombre='Ingenierías')
                    return HttpResponseRedirect('/dashboard/')
                else:
                    print("Invalido")
    return render(request, 'dashboard_contenido.html', context)

@login_required
def dashboardAjustes(request):
    areas = AreaList.objects.filter(activo = True)
    departamentos = DepartamentoList.objects.filter(activo = True)
    context = {
        'nombre_usuario': request.user.nombres,
        'activo_Objeto': "active",
        'areas': areas,
        'departamentos': departamentos
    }
    return render(request, 'dashboard_ajustes.html', context)

@login_required
def dashboardProfesores(request):
    if request.user.rol == 'alumno': 
        return HttpResponseRedirect("/home/")
    elif request.user.rol == 'profesor':  
        return HttpResponseRedirect("/dashboard/")    
    else: 
        exito = False
        if request.method == "POST" and "addprofesor" in request.POST:
            usuario = request.POST.get('nvprof_Username','')
            contra = request.POST.get('nvprof_Contrseña','')  
            nombre = request.POST.get('nvprof_Nombre','')
            apellido = request.POST.get('nvprof_Apellidos','')
            correo = request.POST.get('nvprof_Correo','')   
            institucion = request.POST.get('nvprof_Institucion','')
            departamento = request.POST.get('nvprof_Departamento','')
            rfc = request.POST.get('nvprof_RFC','')
            telefono = request.POST.get('nvprof_Telefono','')
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
                        usm.departamento(departamento)
                        usm.rfc(rfc)
                        usm.save()    
                        messages.success(request, "El usuario se registró con exito")
                        exito = True
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
                        usm.departamento(departamento)
                        usm.rfc(rfc)
                        usm.save()   
                        messages.success(request, "El usuario se registró con exito")
                        exito = True
            else:
                usm = Usuario.objects.create_profesor_user(correo,usuario,nombre,apellido,contra,telefono,rfc,institucion,departamento)
                usm.save()
                messages.success(request, "El usuario se registró con exito")
                exito = True
        profesores = Usuario.objects.filter(rol = 'profesor')
        departamentos = DepartamentoList.objects.filter(activo = True)
        context = {
            'nombre_usuario': request.user.nombres,
            'activo_profesores': "active",
            'exito': exito,
            'profesores': profesores,
            'departamentos': departamentos
        }
        return render(request, 'dashboard_profesores.html', context)

@login_required
def dashboardAdmin(request):
    if request.user.rol == 'alumno': 
        return HttpResponseRedirect("/home/")
    elif request.user.rol == 'profesor':  
        return HttpResponseRedirect("/dashboard/")    
    else:    
        
        context = {
            'nombre_usuario': request.user.nombres,
            'activo_general': "active",
            'contador_objetos': Objeto.objects.filter(estatus = 'activo').count(),
            'contador_alumnos': Usuario.objects.filter(rol = 'alumno').count(),
            'contador_maestros': Usuario.objects.filter(rol = 'profesor').count()
        }      
        return render(request, 'dashboard_admin.html', context)

@login_required
def objeto(request):
    if request.session.has_key('idobjeto'):
        idobjeto = request.session.get('idobjeto')
        if request.user.rol == 'alumno': profesor = False
        else: profesor = True
        consulta = Objeto.objects.get(idobjeto = idobjeto)
        areas = Area.objects.filter(idobjeto = idobjeto)
        context = {
            'nombre_usuario': request.user.nombres,
            'apellidos_usuario': request.user.apellidos,
            'profesor': profesor,
            'consulta': consulta,
            'areas': areas
        }
        if request.method == "POST" and "desc" in request.POST:
            obj = Objeto.objects.get(idobjeto = request.POST.get('desc',''))
            descargas = getattr(obj, 'descargas')
            descargas += 1
            obj.descargas = descargas
            obj.save()
        return render(request, 'objeto.html', context)

