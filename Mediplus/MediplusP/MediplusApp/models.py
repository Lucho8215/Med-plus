from django.db import models

class Medicos(models.Model):
    Id_Medico= models.BigIntegerField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Telefono = models.BigIntegerField()
    Especialidad = models.CharField(max_length=50)

class Pacientes(models.Model):
    Cedula = models.BigIntegerField(primary_key=True)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    FechaNto = models.DateField()
    Edad = models.IntegerField()
    Telefono = models.BigIntegerField()
    Direccion = models.CharField(max_length=50)
    Contacto = models.CharField(max_length=50)
    Parentezco = models.CharField(max_length=50)
    Tel_Contacto = models.BigIntegerField()
    Medicos= models.ForeignKey(Medicos, on_delete=models.CASCADE)
