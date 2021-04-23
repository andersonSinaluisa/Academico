from django.contrib import admin
from django.urls import path
from cfg.views import login, inicio, ModuloCrear, ModuloListar, ModuloEditar, \
    MenuListar, MenuCrear, MenuEditar

urlpatterns = [
    path('', login, name='login'),
    path('inicio/', inicio, name='inicio'),
    path('crear-modulo/', ModuloCrear.as_view(), name='crear_modulo'),
    path('modulos/', ModuloListar.as_view(), name='modulos'),
    path('editar-modulo/<int:pk>', ModuloEditar.as_view(), name='editar_modulo'),
    path('menus/', MenuListar.as_view(), name='menus'),
    path('crear-menu/', MenuCrear.as_view(), name='crear_menu'),
    path('editar-menu/<int:pk>', MenuEditar.as_view(), name='editar_menu')
]
