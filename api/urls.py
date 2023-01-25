from django.urls import path
from .views import ProductoList, UsuarioList, ProductoDetail, UsuarioDetail

urlpatterns = [
    path('initProducts/',ProductoList.as_view()),
    path('initUsers/',UsuarioList.as_view()),
    path('users/<str:pk>',UsuarioDetail.as_view()),
    path('prodById/<int:pk>',ProductoDetail.as_view()),
]