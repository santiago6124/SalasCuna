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
        return f"{self.caracteristica}"

class TipoBarrio(models.Model):
    # barrio de chico en sala cuna
    barrio = models.CharField(max_length=100)

    def __str__(self):
        return self.barrio


class Madre(models.Model):
    # Apellido y nombre de madre de chico
    dni = models.IntegerField(primary_key=True)
    apellido_y_nombre = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.apellido_y_nombre}"

class Chico(models.Model):
    dni = models.IntegerField(primary_key=True)
    sala_cuna = models.ForeignKey(SalaCuna, on_delete=models.CASCADE )
    apellido = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    sexo = models.ForeignKey(TipoSexo, on_delete=models.CASCADE )
    calle = models.CharField(max_length=40)
    numero_calle = models.IntegerField()
    barrio = models.ForeignKey( TipoBarrio, on_delete=models.CASCADE )
    localidad = models.ForeignKey(TipoLocalidad, on_delete=models.CASCADE )
    estado = models.ForeignKey(TipoEstado, on_delete=models.CASCADE )
    turno = models.ForeignKey(TipoTurno, on_delete=models.CASCADE )
    caracteristica = models.ForeignKey(TipoCaracteristicaTel, on_delete=models.CASCADE )
    numero_telefono = models.IntegerField()
    madre = models.ForeignKey(Madre, on_delete=models.CASCADE )
    
    def __str__(self):
        return f"{self.apellido} {self.nombre} {self.calle} {self.numero_calle} {self.numero_telefono} {self.dni} {self.fecha_nacimiento} {self.sala_cuna} {self.estado} {self.turno} {self.madre} {self.sexo} {self.localidad} {self.barrio}   "

# manage.py runserver
