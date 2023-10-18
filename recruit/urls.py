from rest_framework.routers import DefaultRouter
from .views import RecruitViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'recruitment', RecruitViewSet, basename='recruitment')

urlpatterns = [
    path('', include(router.urls), name='recruit'),
]
