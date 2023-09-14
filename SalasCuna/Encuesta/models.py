from django.db import models

# Create your models here.


class Encuesta(models.Model):
    name =  models.CharField(max_length=255, blank=False)

class TipoPregunta(models.Model):
    tipoPregunta =  models.CharField(max_length=255, blank=False)

class Pregunta(models.Model):
    name =  models.CharField(max_length=255, blank=False)
    parentQuestion = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    tipoPregunta = models.ForeignKey(
        "TipoPregunta", on_delete=models.CASCADE, blank=False, null=False
    )
    encuesta = models.ForeignKey(
        "Encuesta", on_delete=models.CASCADE, blank=False, null=False
    )


class TipoRepuesta(models.Model):
    tipoRepuesta =  models.CharField(max_length=255, blank=False)

class Repuesta(models.Model):
    name =  models.CharField(max_length=255, blank=False)
    pregunta = models.ForeignKey(
        "Pregunta", on_delete=models.CASCADE, blank=False, null=False
    )
    tipoRepuesta = models.ForeignKey(
        "TipoRepuesta", on_delete=models.CASCADE, blank=False, null=False
    )

    
