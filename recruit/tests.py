
from rest_framework.test import APITestCase, APITransactionTestCase
from django.urls import reverse

from rest_framework.test import APIClient

from .models import Recruit
from company.models import Company, User


# Create your tests here.
# superuser로 값을 넣어 놨습니다.
# 임의로 정해놓은 User에 { 1 : '홍길동', 2 : '박영식' } 데이터를 넣어 놨습니다.
# 또한 임의로 지정한 Company model에 { 1 : '네이버', 2 : '원티드' } 데이터를 넣어 놨습니다.

# 1. 채용관련 test Notion에 올라와 있는 요구 사항 순서에 맞게 test를 진행 하였습니다.
class RecruitTest(APITransactionTestCase):
    
    def setUp(self):
        self.client = APIClient()
        #임의로 넣어 놓는 회사 데이터 베이스
        self.test_data_com1 = Company.objects.create(company_id=1, company_name="네이버", country='대한민국', region='판교')
        self.test_data_com2 = Company.objects.create(company_id=2, company_name="원티드랩",  country='대한민국', region='서울')
        self.test_data_com3 = Company.objects.create(company_id=3, company_name="원티드코리아",  country='대한민국', region='부산')
        
        #임의로 넣어 놓는 채용공고 데이터 베이스
        self.test_data_re1 = Recruit.objects.create(recruit_id=1, company_id=self.test_data_com2, recruit_position='백엔드 주니어 개발자', recruit_compensation=15000000, recruit_con='원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..', recruit_skills='Python')
        self.test_data_re2 = Recruit.objects.create(recruit_id=2, company_id=self.test_data_com1, recruit_position='Django 백엔드 개발자', recruit_compensation=20000000, recruit_con='5년 경력 이상 Spring Backend', recruit_skills='Django')
        self.test_data_re3 = Recruit.objects.create(recruit_id=3, company_id=self.test_data_com1, recruit_position='주니어 백앤드', recruit_compensation=13000000, recruit_con='Django Backend', recruit_skills='Django, Python')
        self.test_data_re4 = Recruit.objects.create(recruit_id=4, company_id=self.test_data_com1, recruit_position='Spring 백엔드 개발자', recruit_compensation=20000000, recruit_con='8년 경력 이상 Spring Backend', recruit_skills='Spring, java')
        self.test_data_re5 = Recruit.objects.create(recruit_id=5, company_id=self.test_data_com3, recruit_position='프론트 주니어 개발자', recruit_compensation=15000000, recruit_con='원티드코리아에서 프론트 주니어 개발자를 채용합니다. 자격요건은..', recruit_skills='React')
        
        self.search = ['Django', '원티드']
        self.result = [2, 2]
        
        self.naver_list = [2, 3, 4]
    # 1. 채용공고를 등록하는 요구사항 test
    def test_recruit_post_success(self):
        data = {
            "company_id": 2,
            "recruit_position": "주니어 벡엔드",
            "recruit_compensation": 10000000,
            "recruit_con": "네이버에서 백앤드 개발자를 채용합니다.",
            "recruit_skills": "Python"
        }
        
    # post 함수에 대한 테스트이기 때문에 post로 작성을 한다.
	# format을 json으로 지정해 줍니다.
        response = self.client.post('/recruit/recruitment/', data=data, format='json')
	# 반환되는 status_code와 message가 같은지 비교하여 같을 경우 테스트에서 OK를 띄워준다.
        self.assertEqual(response.status_code, 201)
    #채용공고 목록 return하는 test
    
    # 2. 채용 공고를 수정하는 요구사항 test
    def test_update_patch_success(self):
        dataset = [
            {
                "company_id": 2,
                "recruit_position":"백엔드 주니어 개발자",
                "recruit_compensation":1500000, # 변경됨
                "recruit_con":"원티드랩에서 백엔드 주니어 개발자를 '적극' 채용합니다. 자격요건은..", # 변경됨
                "recruit_skills":"Python"
            },
            {
                "company_id": 2,
                "recruit_position":"백엔드 주니어 개발자",
                "recruit_compensation":1000000,
                "recruit_con":"원티드랩에서 백엔드 주니어 개발자를 채용합니다. 자격요건은..",
                "recruit_skills":"Django" # 변경됨
            }
        ]
        #각 변수에 다른 값을 넣어 주는데 patch시 그 값으로 변경되어 return하는지 확인
        for data in dataset:
            response = self.client.patch('/recruit/recruitment/1/', data=data, format='json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['recruit_compensation'], data['recruit_compensation'])
            self.assertEqual(response.data['recruit_con'], data['recruit_con'])
            self.assertEqual(response.data['recruit_skills'], data['recruit_skills'])
    # 3. 채용공고를 삭제하는 요구 사항
    def test_delete_patch_succes(self):
        response = self.client.delete('/recruit/recruitment/4/')
        self.assertEqual(response.status_code, 204)
    
    # 4-1. 채용공고 목록을 가지고 오는 요구 사항
    def test_register_get_success(self):
    # get 함수에 대한 테스트이기 때문에 get로 작성을 한다.
        response = self.client.get('/recruit/recruitment/')
		
	# 반환되는 status_code와 message가 같은지 비교하여 같을 경우 테스트에서 OK를 띄워준다.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    # 4-2. 채용공고를 검색하는 기능 구현 요구사항 테스트 
    #Django를 검색 했을때는 2개의 결과 값이 나와야하고, 원티드를 검색한 결과는 원티드랩과 원티드 코리아가 공고를 각각 하나씩올렸으니 2개가 나와야한다.
    def test_search_get_success(self):
    # get 함수에 대한 테스트이기 때문에 get로 작성을 한다.
	# 반환되는 status_code와 message가 같은지 비교하여 같을 경우 테스트에서 OK를 띄워준다.
        for s, res in zip(self.search, self.result):
            
            response = self.client.get(f'/recruit/recruitment/?search={s}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), res)
    
    # 5. 채용 상세 페이지를 가지고 오는 요구사항을 test    
    def test_retrieve_get_success(self):
        #네이버가 올린 공고를 확인 여기서 네이버는 3개의 채용공고를 올린 것을 확인 할 수 있습니다.
        # 네이버가 올린 채용공고의 리스트는 [2, 3, 4]
        response = self.client.get('/recruit/recruitment/2/')
        self.assertEqual(response.status_code, 200)
        # 상세보기 페이지에서 Response에 "채용내용"이 추가적으로 담겨져 있는지 확인
        self.assertEqual(response.data['recruit_con'], self.test_data_re2.recruit_con)
        # 상세보기 페이지에서 Response에 해당 회사가 올린 다른 채용골고가 추가적으로 포함 되어 있는지 확인
        self.assertEqual(response.data['related_recruit_ids'], self.naver_list)
        
        
    