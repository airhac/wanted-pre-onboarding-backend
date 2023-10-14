from django.db import models

# Create your models here.
# 회사 데이터 베이스
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    contry = models.CharField(default='', max_length=100, null=False, blank=False)
    region = models.CharField(default='', max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.company_name