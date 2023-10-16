from django.db import models
from company.models import Company

class Recruit(models.Model):
    #채용공고_id
    recruit_id = models.AutoField(primary_key=True, verbose_name='채용공고_id')
    #회사_id
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='회사_id')
    #채용포지션
    recruit_position = models.CharField(default='', max_length=100, null=False, blank=False, verbose_name='채용포지션')
    #채용보상금
    recruit_compensation = models.BigIntegerField(default=0, verbose_name='채용보상금')
    #채용내용
    recruit_con = models.CharField(default='', max_length=100, null=False, blank=False, verbose_name='채용내용')
    #사용기술
    recruit_skills = models.CharField(default='', max_length=100, null=False, blank=False, verbose_name='사용기술')
