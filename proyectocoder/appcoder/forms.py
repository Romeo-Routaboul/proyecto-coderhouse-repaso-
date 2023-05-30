from django import forms

class ProfesorFormulario (forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EstudianteFormulario (forms.Form):
    nombre = forms.CharField(min_length=3, max_length=50)
    apellido = forms.CharField(min_length=2, max_length=80)
    email = forms.EmailField()

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()