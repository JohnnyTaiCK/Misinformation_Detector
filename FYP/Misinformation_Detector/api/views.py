from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class UserFeedbackViewSet(viewsets.ViewSet):
    
    def create(self,request):
        return Response({'prediction': "必勝！"})