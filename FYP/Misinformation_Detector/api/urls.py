from django.contrib import admin
from django.urls import path
from .views import UserFeedbackViewSet

urlpatterns = [
    path('', UserFeedbackViewSet.as_view({'post': 'create'})),
]