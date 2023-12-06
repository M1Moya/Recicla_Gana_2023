from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

