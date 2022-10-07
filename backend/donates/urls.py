from django.urls import path, include

from rest_framework import routers

from .views import *

# REST Router 설정
router = routers.SimpleRouter()
router.register(r"donateInfo", DonateInfoViewSet)  # 근로자 근태 정보 URL
router.register(r"foodImage", ImageRegisterViewSet)  # 근로자 근태 정보 URL

urlpatterns = [
    path("api/", include(router.urls)),  # REST API 등록
]