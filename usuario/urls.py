from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

#Urls de app Usuario
urlpatterns = [
    path("recompensa/", login_required(ListRecompensaView.as_view()), name='recompensa'),
    path("recompensa/agregar_recompensa/", login_required(NewRecompensa.as_view()), name='new_recompensa'),
    path("recompensa/<int:pk>/editar_recompensa/", login_required(EditRecompensa.as_view()), name='edit_recompensa'),
    path("recompensa/<int:pk>/eliminar_recompensa/", login_required(DeleteRecompensa.as_view()), name='delete_recompensa')
]
