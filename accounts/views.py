from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from user.forms import FormularioUsuarioNuevo
from user.models import Usuario

# Create your views here.
class SignUpView(CreateView):
    model = Usuario
    form_class = FormularioUsuarioNuevo
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    