from cfg.models import Modulo, Menu

def menus(request):
    modulo = Modulo.objects.all()
    context = {}
    lista = []
    for i in modulo:
        lista.append({'modulo':i,'menus':Menu.objects.filter(id_modulo=i.id_modulo,estado=True)})
    print(lista)
    return {'modulos':lista}
