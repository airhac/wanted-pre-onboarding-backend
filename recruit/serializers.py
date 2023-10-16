from .models import Recruit
from company.models import Company
from rest_framework import serializers

class RecruitSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    #회사_id 값에 대한 회사 이름을 serializer를 통해 보내줍니다.
    def get_company_name(self, obj):
        return obj.company_id.company_name
    
    def get_country(self, obj):
        return obj.company_id.country
    
    def get_region(self, obj):
        return obj.company_id.region
        
    class Meta:
        model = Recruit
        fields = ['recruit_id', 'company_id', 'company_name', 'country', 'region', 'recruit_position', 'recruit_compensation', 'recruit_con', 'recruit_skills']
        