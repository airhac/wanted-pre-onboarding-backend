from django.db import models

# Create your models here.
# 회사 데이터 베이스
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    country = models.CharField(default='', max_length=100, null=False, blank=False)
    region = models.CharField(default='', max_length=100, null=False, blank=False)
    
    
# Create your models here.
#원래 제공해주는 auth_user model이 아닌 임의로 지정해준 user model
class User(models.Model):
    # 1. 사용자의 id 값
    id = models.AutoField(primary_key=True, null=False, blank=False)
    # 2. 사용자의 이름
    user_name = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    