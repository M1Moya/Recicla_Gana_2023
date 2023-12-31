from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from user.models import Usuario
from .models import*

# Create your views here.

#Vista para poder Ver las Recompensas existentes
class ListRecompensaView(ListView):
    model = Canjeables
    template_name = "recompensa_list.html"

#Vista para poder Agregar Nuevas Recompensas
class NewRecompensa(CreateView):
    model = Canjeables
    template_name = "recompensa_new.html"
    fields = ["recompensa", "categoria", "puntos"]
    success_url = reverse_lazy("recompensa")

#Vista para poder Editar las recompensas
class EditRecompensa(UpdateView):
    model = Canjeables
    template_name = "recompensa_edit.html"
    fields = ["recompensa", "categoria", "puntos"]
    success_url = reverse_lazy("recompensa")

#Vista para poder Eliminar una recompensa
class DeleteRecompensa(DeleteView):
    model = Canjeables
    template_name = "recompensa_delete.html"
    success_url  = reverse_lazy("recompensa")

#Vista para poder Ver los Materiales Reciclables existentes
class ListMaterialView(ListView):
    model = Material
    template_name = "material_list.html"

#Vista para poder Editar los Materiales Reciclables
class EditMaterial(UpdateView):
    model = Material
    template_name = "material_edit.html"
    fields = ["material", "valor_puntos"]
    success_url = reverse_lazy("material")

#Vista para poder Eliminar un Material Reciclable
class DeleteMaterial(DeleteView):
    model = Material
    template_name = "material_delete.html"
    success_url  = reverse_lazy("material")

#Vista para poder Agregar nuevos Materiales Reciclables
class NewMaterial(CreateView):
    model = Material
    template_name = "material_new.html"
    fields = ["material", "valor_puntos"]
    success_url = reverse_lazy("material")

#Vista para poder Ver los Usuarios
class ListUsuarios(ListView):
    model = Usuario
    template_name = "usuario_list.html"

#Vista de Suma de Puntos al Usuario
class SumaPuntos(UpdateView):
    model = Usuario
    template_name = 'usuario_suma_puntos.html'
    fields = ['email', 'nombre', 'apellido', 'puntos']
    success_url = reverse_lazy('usuarios')