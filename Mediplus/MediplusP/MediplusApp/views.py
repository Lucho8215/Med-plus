import json
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotAllowed

from .models import Medicos, Pacientes

def mediplus(request):
    return HttpResponse("Bienvenido a Mediplus:\nSoftware de atencion médica")


def agregar_paciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tratante = Medicos.objects.filter(Id_Medico = data["Id_Medico"]).first()
            if (not tratante):
                return HttpResponseBadRequest("El Medico asignado no existe")
            paciente = Pacientes(
                Cedula = data["Cedula"],
                Nombres = data["Nombres"],
                Apellidos = data["Apellidos"],
                FechaNto = data["FechaNto"],
                Edad = data["Edad"],
                Telefono = data["Telefono"],
                Direccion = data["Direccion"],
                Contacto = data["Contacto"],
                Parentezco = data["Parentezco"],
                Tel_Contacto = data["Tel_Contacto"],
                Medicos = tratante
                            )
            paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def agregar_medico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            medico = Medicos(
                Id_Medico = data["Id_Medico"],
                Nombres = data["Nombres"],
                Apellidos = data["Apellidos"],
                Telefono = data["Telefono"],
                Especialidad = data["Especialidad"]
                )
            medico.save()
            return HttpResponse("Nuevo Medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Metodo invalido")

def datos_paciente(request, numero):
    if request.method == 'GET':
        datos = Pacientes.objects.filter(Cedula = numero).first()
        if (not datos):
            return HttpResponseBadRequest("El paciente con este documento no esta en la lista")
        #tratante = Medicos.objects.filter(Id_Medico = data["Id_Medico"]).first()
        #if (not tratante):
           # return HttpResponseBadRequest("El Medico asignado no existe")
        data = {
                "Cedula": datos.Cedula,
                "Nombres": datos.Nombres,
                "Apellidos": datos.Apellidos,
                "FechaNto": str(datos.FechaNto),
                "Edad": datos.Edad,
                "Telefono": datos.Telefono,
                "Direccion": datos.Direccion,
                "Contacto": datos.Contacto,
                "Parentezco": datos.Parentezco,
                "Tel_Contacto": datos.Tel_Contacto,
                #"Medico": datos.Medicos
                }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'],"Metodo Inválido")

def lista_pacientes(request):
    if request.method == 'GET':
        datos = Pacientes.objects.all()
        if (not datos):
            return HttpResponseBadRequest("No hay pacientes en la base de datos")
        info = []
        for x in datos:
            data = {
                "Cedula": x.Cedula,
                "Nombres": x.Nombres,
                "Apellidos": x.Apellidos,
                "FechaNto": str(x.FechaNto),
                "Edad": x.Edad,
                "Telefono": x.Telefono,
                "Direccion": x.Direccion,
                "Contacto": x.Contacto,
                "Parentezco": x.Parentezco,
                "Tel_Contacto": x.Tel_Contacto,
                "Id_Medico": x.Id_Medico
                }
            info.append(data)
        dataJson = json.dumps(info)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Metodo invalido")
