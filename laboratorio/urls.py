from django.urls import path
from .views import (
    insertar_lab, mostrar_lab, editar_lab, eliminar_lab
)

urlpatterns = [
    path('', insertar_lab, name='insertar-lab'),
    path('mostrar/', mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>/', editar_lab, name='editar-lab'),
    path('eliminar/<int:pk>/', eliminar_lab, name='eliminar-lab'),
]
