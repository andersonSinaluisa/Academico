from django.db import models


class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20, blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Modulo",
        verbose_name_plural = "Modulos",
        db_table = "cfg_modulo"
        ordering = ["codigo"]

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=False, null=False, unique=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Menu',
        verbose_name_plural = 'Menus',
        db_table = 'cfg_menu'
        ordering = ['orden']

