from django.urls import path
from .views import *

#Vistas de las paginas de la app Home
urlpatterns = [
    path('', HomeView.as_view(), name="home")
]