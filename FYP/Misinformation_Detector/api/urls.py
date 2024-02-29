from django.contrib import admin
from django.urls import path
from .views import DetectionViewSet

urlpatterns = [
    path('', DetectionViewSet.as_view({'post': 'create'})),
]