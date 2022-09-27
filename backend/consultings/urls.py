from django.urls import path, include

from rest_framework import routers

from .views import *


# REST Router 설정
router = routers.SimpleRouter()
router.register(r"player", PlayerViewSet)  # 컨설팅 선수 정보 URL
router.register(r"image", ImageRegisterViewSet) # 프로필 추가 URL


urlpatterns = [
    path("api/", include(router.urls)),  # REST API 등록
    path("create_user/", create_random_user), # 컨설팅 선수 가데이터 생성
]
