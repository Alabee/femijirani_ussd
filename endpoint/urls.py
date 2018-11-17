from django.urls import path, include
from . import views

urlpatterns = [
    path('jirani/', views.index),
]
