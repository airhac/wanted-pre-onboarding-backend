from .models import Recruit
from company.models import Company
from rest_framework import serializers

class RecruitSerializer(serializers.ModelSerializer):
    #회사_id 관련된 데이터는 수정이 불가 일기만 가능합니다.
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
        
        
class RecruitDetailSerializer(serializers.ModelSerializer):
    #회사_id 관련된 데이터는 수정이 불가 일기만 가능합니다.
    company_id = serializers.PrimaryKeyRelatedField(read_only=True)
    company_name = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    
    related_recruit_ids = serializers.SerializerMethodField()
    #회사_id 값에 대한 회사 이름을 serializer를 통해 보내줍니다.
    def get_company_name(self, obj):
        return obj.company_id.company_name
    
    def get_country(self, obj):
        return obj.company_id.country
    
    def get_region(self, obj):
        return obj.company_id.region

    def get_related_recruit_ids(self, obj):
        # 해당 company_id로 지원한 지원공고인 recruit_id를 리스트로 반환
        related_recruits = Recruit.objects.filter(company_id=obj.company_id)
        recruit_ids = related_recruits.values_list('recruit_id', flat=True)
        return list(recruit_ids)
    
    class Meta:
        model = Recruit
        fields = ['recruit_id', 'company_id', 'company_name', 'country', 'region', 'recruit_position', 'recruit_compensation', 'recruit_con', 'recruit_skills', 'related_recruit_ids']
        