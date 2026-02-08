from django.urls import path
from . import views

app_name = 'meal_plan'
urlpatterns = [
    # Home
    path('', views.index, name='index')
]