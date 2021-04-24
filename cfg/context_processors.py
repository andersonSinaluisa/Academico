from cfg.models import Modulo, Menu

def menus(request):
    modulo = Modulo.objects.filter(estado=True).order_by('orden')
    context = {}
    lista = []
    for i in modulo:
        if request.user.is_superuser:
            lista.append({'modulo':i,'menus':Menu.objects.filter(id_modulo=i.id_modulo,estado=True)})
        else:
            for a in request.user.user_permissions.all():
                lista.append({'modulo':i,'menus':Menu.objects.filter(id_modulo=i.id_modulo,estado=True,permiso=a)})
      
    print(request.user.user_permissions.all())
    return {'modulos':lista}
