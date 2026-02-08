from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home
    path('', views.index, name='index')
]