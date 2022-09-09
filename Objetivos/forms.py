from django import forms
from Objetivos.models import Area, Objeto, Usuario

class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        exclude = ('idobjeto',)

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        exclude = ('idarea',)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ('username', 'password', 'imagen',)
