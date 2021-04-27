from cfg.models import Modulo, Menu


def menus(request):
    modulo = Modulo.objects.filter(estado=True).order_by('orden')
    lista = []
    lista_menus = []
    if request.user.is_superuser:
        for i in modulo:
            lista.append({'modulo': i, 'menus': Menu.objects.filter(id_modulo=i.id_modulo, estado=True)})
    else:
        permiso = request.user.groups.all().first()
        if permiso:
            for b in permiso.permissions.all():
                menu = Menu.objects.filter(estado=True, permiso=b).first()
                if menu:
                    lista_menus.append(menu.id_menu)
        for i in modulo:
            m = Menu.objects.filter(id_menu__in=lista_menus, id_modulo=i.id_modulo, estado=True)
            if m:
                lista.append({'modulo': i, 'menus': m})

    return {'modulos': lista}
