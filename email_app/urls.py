from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.send_simple_email, name='email'),
    path('contact/', contact_view, name='contact'),

]
