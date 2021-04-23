from django.urls import path
from mant.views import *

urlpatterns = [
    path("personas/", PersonaListar.as_view(), name="personas"),
    path("crear-persona/", PersonaCrear.as_view(), name="crear_persona"),
    path("editar-persona/<int:pk>", PersonaEditar.as_view(), name="editar_persona"),
]
