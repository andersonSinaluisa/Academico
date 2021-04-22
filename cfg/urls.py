from django.contrib import admin
from django.urls import path
from cfg.views import login, inicio

urlpatterns = [
    path('', login, name='login'),
    path('inicio',inicio, name='inicio')
]
