from django.urls import path
from api import views

urlpatterns = [
    path('home', views.api_home, name='api-home')
]