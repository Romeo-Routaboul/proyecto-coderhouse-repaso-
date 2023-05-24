from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def vista_saludo(request):
    return HttpResponse("Hola coders")

def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy} - Bienvenid@ {nombre}"
    return HttpResponse (respuesta)

def anio_nacimiento(request, anio):
    anio = int(anio)
    respuesta = datetime.now().year - anio
    return HttpResponse (f"naciste en el año {respuesta}")

def vista_plantilla(request):
    # Creamos la plantilla
    archivo = open(r"C:\Users\rome2\OneDrive\Escritorio\Coderhouse\repaso\Django\proyectocoder\proyectocoder\templates\plantilla_bonita.html")
    
    #creamos el objeto "plantilla"
    plantilla = Template(archivo.read())

    #Cerramos el archivo para liberar recursos
    archivo.close()

    # Diccionario con datos para la plantilla
    datos = {"nombre": "Leonel", "fecha": datetime.now(), "apellido": "Gareis"}

    # Creamos el contexto
    contexto = Context(datos)

    # Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def ver_alumnos(request):
    archivo = open(r"C:\Users\rome2\OneDrive\Escritorio\Coderhouse\repaso\Django\proyectocoder\proyectocoder\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    alumnos = ["Leonel Gareis", "Romeo Routaboul", "Emiloiano Martinez", "Fernando Redondo"]

    datos = {"tecnologia": "Carpinteria", "listado_alumnos": alumnos}
 
    contexto = Context(datos)

    documento = plantilla.render(contexto)

    return HttpResponse(documento)

def ver_alumnos2(request):
    alumnos = ["Leonel Gareis", "Romeo Routaboul", "Emiloiano Martinez", "Fernando Redondo"]
    
    datos = {"tecnologia": "Python", "listado_alumnos": alumnos}

    plantilla = loader.get_template("lsitado_alumnos.html")
    
    documento = plantilla.render(datos)

    return HttpResponse(documento)