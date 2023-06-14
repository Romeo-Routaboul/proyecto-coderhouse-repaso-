from django.shortcuts import render, redirect
from django.http import HttpResponse
from appcoder.models import*
from appcoder.forms import ProfesorFormulario, EstudianteFormulario, CursoFormulario, UserRegisterForm

from proyectocoder.settings import BASE_DIR
import os

# Class-Based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def inicio (request):
    return render (request, "appcoder/index.html")

def estudiantes(request):
    return render (request, "appcoder/estudiantes.html")

def profesores(request):
    return render (request, "appcoder/profesores.html")

def cursos(request):
    #validamos el tipo de peticion
    if request.method == "POST":

        #cargamos los datos en el formulario
        formulario = CursoFormulario(request.POST)

        #validamos los datos
        if formulario.is_valid():

            #recuperamos los datos "limpios"
            data = formulario.cleaned_data

            #creamos el curos
            curso = Curso(nombre=data["nombre"], camada=data["camada"])

            #guardamos
            curso.save()

    cursos = Curso.objects.all()

    #creamos el formulario vacio
    formulario = CursoFormulario()

    contexto = {"listado_cursos": cursos, "formulario": formulario}


    return render (request, "appcoder/cursos.html", contexto)

def editar_curso(request, id):
    curso= Curso.objects.get(id = id)

    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre = data["nombre"]
            curso.camada = data["camada"]
            curso.save()
            return redirect ("coder-cursos")
        else:
            return render (request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": formulario.errors })
            

    else:
        formulario = CursoFormulario(initial={"nombre":curso.nombre, "camada": curso.camada })
        return render (request, "appcoder/editar_curso.html", {"formulario": formulario, "errores": "" })

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect ("coder-cursos")

def entregables(request):
    return render (request, "appcoder/entregables.html")


def crear_profesor(request):

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido = data["apellido"], email= data["email"], profesion= data ["profesion"])
            profesor.save()

    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}
    return render (request, "appcoder/crearprofe.html", contexto)

def buscar_curso(request):

    return render (request, "appcoder/buscarcurso.html")

def resultados_busqueda_cursos(request):

    nombre_curso = request.GET["nombre_curso"]

    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder/resultados_busqueda_cursos.html", {"cursos": cursos})

def crear_estuduiante(request):

    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            estudiante = Estudiante(nombre= data["nombre"], apellido= data["apellido"], email= data["email"] )
            estudiante.save()

    formulario = EstudianteFormulario()
    contexto = {"formulario":formulario}
    return render (request, "appcoder/crear_estudiante.html", contexto)

def buscar_estudiante(request):
    if request.GET:
        estudiante = Estudiante.objects.filter(nombre__icontains=request.GET["nombre_alumno"])
        return render (request, "appcoder/busqueda_estudiantes.html", {"listado_alumnos": estudiante})
    return render (request, "appcoder/busqueda_estudiantes.html", {"listado_alumnos":[]})


class EntregablesList(ListView):
    model = Entregable
    template_name = "appcoder/list_entregables.html"

class EntregableDetail(DetailView):
    model = Entregable
    template_name = "appcoder/detail_entregable.html"

class EntregableCreate(CreateView):
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]

class EntregableUpdate(UpdateView):
    model = Entregable
    success_url = "/coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]

class EntregableDelete(DeleteView):
    model = Entregable
    success_url = "coder/entregables/"


class profesoresList(ListView):
    model = Profesor
    template_name = "appcoder/list_profesores.html"

class profesoresDetail(DetailView):
    model = Profesor
    template_name = "appcoder/detail_profesores.html"

class profesoresCreate(CreateView):
    model = Profesor
    success_url = "/coder/profesores/"
    fields = ["nombre", "apellido", "email", "profesion"]

class profesoresUpdate(UpdateView):
    model = Profesor
    success_url = "/coder/profesores/"
    fields = ["nombre", "apellido", "email", "profesion"]

class profesoresDelete(DeleteView):
    model = Profesor
    success_url = "/coder/profesores/"

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("coder-inicio")
            else:
                return render(request, "appcoder/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "appcoder/login.html", {"form": formulario, "errors": formulario.errors})
   
    formulario = AuthenticationForm()
    return render(request, "appcoder/login.html", {"form": formulario, "errors":errors})

def registrar_usuario(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():

            formulario.save()
            return redirect ("coder-inicio")
        else:
            return render (request, "appcoder/register.html", {"form": formulario, "errors":formulario.errors})

    formulario = UserRegisterForm()
    return render (request, "appcoder/register.html", {"form": formulario})
