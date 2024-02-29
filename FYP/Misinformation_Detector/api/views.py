from rest_framework import viewsets
from rest_framework.response import Response

class DetectionViewSet(viewsets.ViewSet):
    
    def create(self,request):
        return Response({'prediction': "必勝！"})