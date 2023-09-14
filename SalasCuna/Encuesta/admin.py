from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class TipoPreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "tipoPregunta")
    list_filter = ["tipoPregunta"]

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parentQuestion", "tipoPregunta")
    list_filter = ["name", "parentQuestion", "tipoPregunta"]

class TipoRepuestaAdmin(admin.ModelAdmin):
    list_display = ("id", "tipoRepuesta")
    list_filter = ["tipoRepuesta"]

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "tipoRespuesta")
    list_filter = ["name", "tipoRespuesta"]