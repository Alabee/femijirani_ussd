from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('jirani/', views.JiraniList.as_view(), name="jirani"),
    path('agent/', views.AgentCredentialDetail.as_view(), name="agent"),
]

urlpatterns = format_suffix_patterns(urlpatterns)