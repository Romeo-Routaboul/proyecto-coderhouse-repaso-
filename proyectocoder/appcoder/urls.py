from django.urls import path
from appcoder.views import*

urlpatterns = [
path("inicio/", inicio, name="coder-inicio"),
path("estudiantes/", estudiantes, name="coder-estudiantes"),
path("profesores/", profesoresList.as_view(), name="coder-profesores"),
path("cursos/", cursos, name="coder-cursos"),
path("cursos/borrar/<id>/", eliminar_curso, name="coder-cursos-borrar"),
path("cursos/actualizar/<id>/", editar_curso, name="coder-cursos-editar"),
path("crearprofe/", crear_profesor, name="coder-crearprofe"),
path("busquedacurso/", buscar_curso, name="curso-buscar"),
path("resultadosbc/", resultados_busqueda_cursos, name="resultados-bc"),
path("crearestudiante/", crear_estuduiante, name="crear-estudiante"),
path("busquedaestudiante/", buscar_estudiante, name="buscar-estudiante"),
path("entregables/",EntregablesList.as_view(), name="coder-entregables"),
path("entregables/detalle/<pk>/",EntregableDetail.as_view() , name="coder-entregable-detail"),
path("entregables/borrar/<pk>/",EntregableDelete.as_view() , name="coder-entregable-delete"),
path("entregables/actualizar/<pk>/",EntregableUpdate.as_view() , name="coder-entregable-update"),
path("entregables/crear/",EntregableCreate.as_view() , name="coder-entregables-create"),
path("profesores/detalle/<pk>/",profesoresDetail.as_view() , name="coder-profesor-detail"),
path("profesores/actualizar/<pk>/",profesoresUpdate.as_view() , name="coder-profesor-update"),
path("profesores/borrar/<pk>/",profesoresDelete.as_view() , name="coder-profesor-delete"),
path("profesores/crear/", profesoresCreate.as_view(), name="coder-profesor-crear"),
path("login/", iniciar_sesion, name="auth-login"),
path("register/", registrar_usuario, name="auth-register"),
]