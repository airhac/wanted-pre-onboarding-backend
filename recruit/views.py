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
    
    #이 함수를 적용함으로써 detail부분에서는 내용을 볼수 있습니다.
    def get_serializer_class(self):
        # 리스트 액션에서만 recruit_con 필드를 제외한 시리얼라이저를 사용
        if self.action == 'list':
            class ListRecruitSerializer(RecruitSerializer):
                class Meta(RecruitSerializer.Meta):
                    fields = [field for field in RecruitSerializer.Meta.fields if field != 'recruit_con']
            return ListRecruitSerializer
        return RecruitSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
        