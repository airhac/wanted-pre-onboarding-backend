from django.db import models
from company.models import User
from recruit.models import Recruit
# Create your models here.
class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True, verbose_name='지원_id')
    # 지원 하나당 사용자 한명만 지원 가능 
    # 지원자가 또 지원 하려고 하면 
    '''
        
    {
        "user_id": [
            "apply with this 사용자_id already exists."
        ]
    }
    와 같이 return 합니다.
    '''
    user_id = models.OneToOneField(User, verbose_name="사용자_id", on_delete=models.CASCADE)
    recruit_id = models.ForeignKey(Recruit, verbose_name="채용공고_id", on_delete=models.CASCADE)
    
    