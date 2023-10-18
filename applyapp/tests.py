from rest_framework.test import APITestCase, APITransactionTestCase
from django.urls import reverse

from rest_framework.test import APIClient

from .models import Apply
from company.models import Company, User
from recruit.models import Recruit
# Create your tests here.
class ApplyTest(APITransactionTestCase):
    
    def setUp(self):
        self.client = APIClient()
        
        # 임의로 넣어 놓은 user 데이터 베이스
        self.test_data_user1 = User.objects.create(id=1, user_name="홍길동")
        self.test_data_user2 = User.objects.create(id=2, user_name="박영식")
        
        #임의로 넣어 놓는 회사 데이터 베이스
        self.test_data_com1 = Company.objects.create(company_id=1, company_name="네이버", country='대한민국', region='판교')
        self.test_data_com2 = Company.objects.create(company_id=2, company_name="원티드랩",  country='대한민국', region='서울')
        self.test_data_com3 = Company.objects.create(company_id=3, company_name="원티드코리아",  country='대한민국', region='부산')
        
        #임의로 넣어 놓는 채용공고 데이터 베이스
        self.test_data_re1 = Recruit.objects.create(recruit_id=1, company_id=self.test_data_com2, recruit_position='백엔드 주니어 개발자', recruit_compensation=15000000, recruit_con='원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..', recruit_skills='Python')
        self.test_data_re2 = Recruit.objects.create(recruit_id=2, company_id=self.test_data_com1, recruit_position='Django 백엔드 개발자', recruit_compensation=20000000, recruit_con='5년 경력 이상 Spring Backend', recruit_skills='Django')
        
        #임의로 넣어 놓은 지원 데이터 베이스
        self.test_data_app1 = Apply.objects.create(apply_id=1, user_id=self.test_data_user1, recruit_id=self.test_data_re1)
    # 6. 사용자는 채용공고에 지원합니다.  
    #이전에 지원한적이 없는 사용자가 지원 가능한 요구사항 테스트
    def test_apply_post_success(self):
        data = {
            "recruit_id": 2,
            "user_id": 2
        }
        response = self.client.post('/apply/application/', data=data, format='json')
        self.assertEqual(response.status_code, 201)
        
    # 이전에 진원한 적이 있어 더이상 지원이 불가능한 요구사항 테스트
    # 사용자는 1회만 지원 가능하도록 되어있음
    # 현재 user1은 채용공고 1에 지원한 상태이다
    def test_apply_post_fail(self):
        data = {
            "recruit_id": 2,
            "user_id": 1
        }
        response = self.client.post('/apply/application/', data=data, format='json')
        error = str(response.data['user_id'][0])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(error, "apply with this 사용자_id already exists.")
        
    def test_do_not_exist_post_fail(self):
        data = {
            "recruit_id": 3,
            "user_id": 1
        }
        response = self.client.post('/apply/application/', data=data, format='json')
        error = str(response.data['recruit_id'][0])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(error, f"Invalid pk \"{data['recruit_id']}\" - object does not exist.")