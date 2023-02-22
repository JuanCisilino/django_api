from django.urls import path
from .views import ProductoList, UsuarioList, ProductoDetail, UsuarioDetail, home, token, PacienteListCreate, PacienteRetrieveUpdateDestroy, DoctorListCreate, DoctorRetrieveUpdateDestroy, HistoriasListCreate, HistoriasRetrieveUpdateDestroy, VademecumMarcaListCreate, VademecumGenericoListCreate

urlpatterns = [
    path('api/initProducts/',ProductoList.as_view()),
    path('api/initUsers/',UsuarioList.as_view()),
    path('api/users/<str:pk>',UsuarioDetail.as_view()),
    path('api/prodById/<int:pk>',ProductoDetail.as_view()),
    path('api/pacientes/', PacienteListCreate.as_view(), name='Lista de Pacientes'),
    path('api/doctores/', DoctorListCreate.as_view(), name='Lista de Doctores'),
    path('api/paciente/<int:pk>/', PacienteRetrieveUpdateDestroy.as_view(), name='Paciente por DNI'),
    path('api/doctor/<str:pk>/', DoctorRetrieveUpdateDestroy.as_view(), name='Doctor por Email'),
    path('api/historias/', HistoriasListCreate.as_view(), name='Lista de Historias Clinicas'),
    path('api/historias/<int:pk>/', HistoriasRetrieveUpdateDestroy.as_view(), name='Historia clinica por ID'),
    path('api/vademecum_marca/', VademecumMarcaListCreate.as_view(), name='Lista de Vademecum Marca'),
    path('api/vademecum_generico/', VademecumGenericoListCreate.as_view(), name='Lista de Vademecum Generico'),
    path('', home, name='Home'),
    path('api/', token, name='Creacion de usuario token'),
]