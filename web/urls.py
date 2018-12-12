from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('donate/', views.donate, name = 'donate'),
    path('register/', views.register, name='register'),
]
