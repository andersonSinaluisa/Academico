from django.urls import path
from cfg.views import *

urlpatterns = [
    path('', login, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('modulos/', ModuloListar.as_view(), name='modulos'),
    path('crear-modulo/', ModuloCrear.as_view(), name='crear_modulo'),
    path('editar-modulo/<int:pk>', ModuloEditar.as_view(), name='editar_modulo'),
    path('eliminar-modulo/<int:pk>', ModuloEliminar.as_view(), name='eliminar_modulo'),
    path('menus/', MenuListar.as_view(), name='menus'),
    path('crear-menu/', MenuCrear.as_view(), name='crear_menu'),
    path('editar-menu/<int:pk>', MenuEditar.as_view(), name='editar_menu'),
    path('eliminar-menu/<int:pk>', MenuEliminar.as_view(), name='eliminar_menu'),
    path('roles/', PermisosListar.as_view(), name='roles'),
    path('crear-rol/', PermisosCrear.as_view(), name='crear_rol'),
    path('editar-rol/<int:pk>', PermisosEditar.as_view(), name='editar_rol'),
    path('eliminar-rol/<int:pk>', PermisosEliminar.as_view(), name='eliminar_rol'),
    path('general/', GeneralListar.as_view(), name='general'),
    path('crear-general/', GeneralCrear.as_view(), name='crear_general'),
    path('editar-general/<int:pk>', GeneralEditar.as_view(), name='editar_general'),
    path('eliminar-general/<int:pk>', GeneralEliminar.as_view(), name='eliminar_general'),
    path("editar-perfil/", editar_perfil, name="editar_perfil")
]
