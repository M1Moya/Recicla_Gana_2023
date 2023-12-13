from django.shortcuts import render
from django.views.generic import *

# Create your views here.

#Vista de la Pagina Principal
class HomeView(TemplateView):
    template_name = "index.html"