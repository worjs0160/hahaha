from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import *

# REST Router 설정
router = DefaultRouter()
router.register(r"donateInfo", DonateInfoViewSet)  # 기부자 기부내용 정보 URL(이미지는 ID로)
router.register(r"donateAndImageInfo", DonateAndImageInfoViewSet)  # 기부자 기부내용 정보 URL(이미지의 모델까지)
router.register(r"foodImage", FoodImageViewSet)  # 음식 이미지 URL
router.register(r"activityImage", ActivityImageViewSet)  # 활동 이미지 URL


urlpatterns = [
    path("api/", include(router.urls)),  # REST API 등록
]