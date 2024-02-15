from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
class UserFeedbackViewSet(viewsets.ViewSet):
    
    def create(self,request):
        return Response({'prediction': "祝戴澤健順利畢業，找到份好工作，最重要的是全心全意投入到學習編程，開始科學運動，找到女朋友，增值自己！"})