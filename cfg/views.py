from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.models import User
from cfg.backend import EmailBackend
from django.contrib.auth import login as do_login
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = EmailBackend.authenticate(
                            EmailBackend,
                            request,
                            username,
                            password
                        )
        if user is not None:
            do_login(request, user)
            return redirect(reverse_lazy('cfg:inicio'))
        else:
            context['msj'] = _('Usuario y/o contraseña incorrecta')
    return render(request,'login.html',context)

@login_required(login_url='/')
def inicio(request):
    return render(request,'inicio.html')