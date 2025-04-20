from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_simple_email, name='email'),
]
