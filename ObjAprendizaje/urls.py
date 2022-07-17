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
    path('dashboard/', Objetivos.views.dashboardGeneral, name="dashboard"),
    path('dashboard/mi_contenido', Objetivos.views.dashboardContenido, name="dashboardContenido"),
    path('objeto/', Objetivos.views.objeto, name="objeto"),
]
