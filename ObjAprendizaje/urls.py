"""ObjAprendizaje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Objetivos import views
import Objetivos.views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Objetivos.views.home, name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    path('registro/', Objetivos.views.registro, name="registro"),
    path('dashboard/', Objetivos.views.dashboardGeneral, name="dashboardGeneral"),
    path('dashboard/mi_contenido', Objetivos.views.dashboardContenido, name="dashboardContenido"),
    path('objeto/', Objetivos.views.objeto, name="objeto"),
]
