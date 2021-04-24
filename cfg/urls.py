from django.contrib import admin
from django.urls import path
from cfg.views import login, inicio, ModuloCrear, ModuloListar, ModuloEditar, \
    MenuListar, MenuCrear, MenuEditar, PermisosListar, PermisosCrear, PermisosEditar
urlpatterns = [
    path('', login, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('modulos/', ModuloListar.as_view(), name='modulos'),
    path('crear-modulo/', ModuloCrear.as_view(), name='crear_modulo'),
    path('editar-modulo/<int:pk>', ModuloEditar.as_view(), name='editar_modulo'),
    path('menus/', MenuListar.as_view(), name='menus'),
    path('crear-menu/', MenuCrear.as_view(), name='crear_menu'),
    path('editar-menu/<int:pk>', MenuEditar.as_view(), name='editar_menu'),
    path('roles/',PermisosListar.as_view(),name='roles'),
    path('crear-rol/',PermisosCrear.as_view(),name='crear_rol'),
    path('editar-rol/<int:pk>',PermisosEditar.as_view(),name='editar_rol')

]
