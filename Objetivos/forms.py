from django import forms
from Objetivos.models import Area, Objeto, Usuario, AreaList, DepartamentoList

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
        exclude = ('username', 'password', 'rol',)

class AreaListForm(forms. ModelForm):
    class Meta:
        model = AreaList
        exclude = ('idarea', 'activo', 'nombre')

class DepartamentoListForm(forms. ModelForm):
    class Meta:
        model = DepartamentoList
        exclude = ('iddepartamento', 'activo', 'nombre')        