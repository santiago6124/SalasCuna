from django.db import models

# Create your models here.

class SalaCuna(models.Model):
    # codigo sala cuna
    codigo = models.CharField(max_length=8, primary_key=True)
    # nombre sala cuna
    nombre = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.codigo} {self.nombre}"

class TipoSexo(models.Model):
    # sexo de chico ( M - F)
    sexo = models.CharField(max_length=1)
    
    def __str__(self):
        return self.sexo

class TipoTurno(models.Model):
    # turno de chico en sala cuna (mañana - tarde - noche)
    turno = models.CharField(max_length=10)

    def __str__(self):
        return self.turno

class TipoEstado(models.Model):
    # estado de chico en sala cuna (sin modificar - alta - baja)
    estado = models.CharField(max_length=15)

    def __str__(self):
        return self.estado

class TipoLocalidad(models.Model):
    # localidad de chico en sala cuna (CBA - PCIA - ETC)
    localidad = models.CharField(max_length=20)

    def __str__(self):
        return self.localidad


class TipoCaracteristicaTel(models.Model):
    # caracteristica de chico en sala cuna (sin modificar - alta - baja)
    caracteristica = models.IntegerField()

    def __str__(self):
        return self.caracteristica

class TipoBarrio(models.Model):
    # barrio de chico en sala cuna
    barrio = models.IntegerField()

    def __str__(self):
        return self.barrio


class Madre(models.Model):
    # Apellido y nombre de madre de chico
    dni = models.IntegerField(primary_key=True)
    apellido_y_nombre = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.apellido_y_nombre}"

class Chico(models.Model):
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    calle = models.CharField(max_length=40)
    numero_calle = models.IntegerField()
    numero_telefono = models.IntegerField()
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    barrio = models.ForeignKey( TipoBarrio, on_delete=models.CASCADE )
    localidad = models.ForeignKey(TipoLocalidad, on_delete=models.CASCADE )
    estado = models.ForeignKey(TipoEstado, on_delete=models.CASCADE )
    turno = models.ForeignKey(TipoTurno, on_delete=models.CASCADE )
    sexo = models.ForeignKey(TipoSexo, on_delete=models.CASCADE )
    madre = models.ForeignKey(Madre, on_delete=models.CASCADE )
    sala_cuna = models.ForeignKey(SalaCuna, on_delete=models.CASCADE )

