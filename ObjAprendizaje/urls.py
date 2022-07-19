from django.contrib import admin
from django.urls import path, include, re_path
from Objetivos import views
import Objetivos.views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Objetivos.views.home, name="home"),
    path('', LoginView.as_view(template_name='login.html'), name='login'), 
    path('registro/', Objetivos.views.registro, name="registro"),
    path('dashboard/', Objetivos.views.dashboardGeneral, name="dashboard"),
    path('dashboard/mi_contenido', Objetivos.views.dashboardContenido, name="dashboardContenido"),
    path('objeto/', Objetivos.views.objeto, name="objeto"),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)