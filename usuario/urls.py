from .views import *
from django.urls import path

#Urls de app Usuario
urlpatterns = [
    path("recompensa/", ListRecompensaView.as_view(), name='recompensa'),
    path("recompensa/agregar_recompensa/", NewRecompensa.as_view(), name='new_recompensa'),
    path("recompensa/<int:pk>/editar_recompensa/", EditRecompensa.as_view(), name='edit_recompensa'),
    path("recompensa/<int:pk>/eliminar_recompensa/", DeleteRecompensa.as_view(), name='delete_recompensa')
]
