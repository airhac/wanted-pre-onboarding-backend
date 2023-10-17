from django.shortcuts import render
from .models import Apply
# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import ApplySerializer
# Create your views here.
class ApplyListView(APIView):
    
    def get(self, request):
        application = Apply.objects.all()
        # 여러 개의 객체를 serialization하기 위해 many=True로 설정
        serializer = ApplySerializer(application, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = ApplySerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)