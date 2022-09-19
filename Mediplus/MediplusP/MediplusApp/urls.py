from django.urls import path
from . import views

urlpatterns = [
    path('mediplus', views.mediplus, name = 'mediplus'),
    path('agregarPaciente', views.agregar_paciente, name = 'agregarPaciente'),
    path('agregarMedico', views.agregar_medico, name = 'agregarMedico'),
    path('datosPaciente/<int:numero>', views.datos_paciente, name = 'datosPaciente'),
    path('listaPacientes', views.lista_pacientes, name = 'listaPacientes'),
] 