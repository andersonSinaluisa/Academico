from django.db import models
from django.contrib.auth.models import Permission


class Modulo(models.Model):
    """Modelo para generar modulos en el template"""

    id_modulo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Modulo",
        verbose_name_plural = "Modulos",
        ordering = ["codigo"]

    def __str__(self):
        """función que retorna el nombre de
        un objecto Modulo

        Returns:
            [str]: [nombre del modulo]
        """
        return self.nombre


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True)
    estado = models.BooleanField(default=True)
    permiso = models.ForeignKey(Permission,on_delete=models.CASCADE,null=True)
    id_modulo = models.ForeignKey(Modulo,on_delete=models.CASCADE,null=False)

    class Meta:
        verbose_name = 'Menu',
        verbose_name_plural = 'Menus',


class GenrGeneral(models.Model):
    """Tabla general para guardar lista"""


    idgenr_general = models.AutoField(primary_key=True)
    tipo = models.CharField('Tipo',max_length=50, blank=False, null=False)
    codigo = models.CharField('Codigo',max_length=50, blank=False, null=False)
    nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Lista',
        verbose_name_plural = 'Listas',

    def __str__(self):
        """Función que devuelve el nombre de un objecto
        de este modelo

        Returns:
            [str]: nombre del objecto
        """
        return self.nombre

class GenrHistorial(models.Model):
    """Tabla para guardar datos de las acciones de usuarios"""

    id_historial = models.AutoField(primary_key=True)
    modulo = models.CharField(max_length=50, blank=False, null=False)
    accion = models.CharField(max_length=50, blank=False, null=False)
    usuario_mod = models.CharField(max_length=50, blank=False, null=False)
    terminal_mod = models.CharField(max_length=50, blank=False, null=False)
    fecha_mod = models.DateField(blank=False, null=False)
    id_menu = models.ForeignKey(Menu,on_delete=models.CASCADE,blank=False, null=False, related_name="fk_genrhistorial_confmenu", db_column='id_menu')

    class Meta:
        verbose_name = 'Historial',
        verbose_name_plural = 'Historiales',


class MensajePantalla(models.Model):
    """Modelo para poner mensajes en las pantallas"""

    
    id_mensaje = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=50)
    valor = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'MensajePantalla'
        verbose_name_plural = 'MensajePantallas'