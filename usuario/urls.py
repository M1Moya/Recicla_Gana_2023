from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

#Urls de app Usuario
urlpatterns = [
    path("recompensa/", login_required(ListRecompensaView.as_view()), name='recompensa'),
    path("recompensa/agregar_recompensa/", login_required(NewRecompensa.as_view()), name='new_recompensa'),
    path("recompensa/<int:pk>/editar_recompensa/", login_required(EditRecompensa.as_view()), name='edit_recompensa'),
    path("recompensa/<int:pk>/eliminar_recompensa/", login_required(DeleteRecompensa.as_view()), name='delete_recompensa'),
    path("material/", login_required(ListMaterialView.as_view()), name='material'),
    path("material/<int:pk>/editar_material/", login_required(EditMaterial.as_view()), name='edit_material'),
    path("material/<int:pk>/eliminar_material/", login_required(DeleteMaterial.as_view()), name='delete_material'),
    path("material/agregar_material/", login_required(NewMaterial.as_view()), name='new_material'),
    path("usuarios/", login_required(ListUsuarios.as_view()), name='usuarios'),
    path("usuarios/<int:pk>/sumar_puntos", login_required(SumaPuntos.as_view()), name='suma_puntos'),
]
