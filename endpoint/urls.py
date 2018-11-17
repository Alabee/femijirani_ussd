from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('jirani/', views.JiraniList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)