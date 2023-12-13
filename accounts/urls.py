from django.urls import path
from .views import SignUpView

#Urls de la App accounts
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]