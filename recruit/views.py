from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Recruit
from company.models import Company
from .serializers import RecruitSerializer

# Create your views here.
class RecruitViewSet(viewsets.ModelViewSet):
    serializer_class = RecruitSerializer
    
    def get_queryset(self):
        return Recruit.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)
        
        