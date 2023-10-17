from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Recruit
from company.models import Company
from .serializers import RecruitSerializer, RecruitDetailSerializer

# Create your views here.
class RecruitViewSet(viewsets.ModelViewSet):
    serializer_class = RecruitSerializer
    #drf의 filters기능을 통해 ?Search적용
    #get요청에서 search하면 해당 값이 포함한 field에서 해당되면 그 list를 반환 해줌
    filter_backends = [filters.SearchFilter]
    search_fields = ['company_name', 'region', 'recruit_position', 'recruit_con', 'recruit_skills']
     
    def get_queryset(self):
        return Recruit.objects.all()
    
    #이 함수를 적용함으로써 detail부분에서는 내용을 볼수 있습니다.
    def get_serializer_class(self):
        # 리스트 액션에서만 recruit_con 필드를 제외한 시리얼라이저를 사용
        if self.action == 'list':
            class ListRecruitSerializer(RecruitSerializer):
                class Meta(RecruitSerializer.Meta):
                    fields = [field for field in RecruitSerializer.Meta.fields if field not in ['recruit_con']]
            return ListRecruitSerializer
        return RecruitSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RecruitDetailSerializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = RecruitDetailSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)