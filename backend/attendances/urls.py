from django.urls import path, include

from rest_framework import routers

from .views import *


# REST Router 설정
router = routers.SimpleRouter()
router.register(r"empAtt", EmpAttendanceViewSet)  # 근로자 근태 정보 URL
router.register(r"comAtt", ComAttendanceViewSet) # 고용기업 전용 근로자 근태 정보 URL
router.register(r"attType", AttTypeViewSet)  # 근태 유형 URL
router.register(r"userAtt", AttendanceUserViewSet)  # 선수 별 근태 정보 URL
router.register(r"userAttType", AttTypeUserViewSet)  # 선수 별 근태 유형 URL
router.register(r"ipRegister", IPRegisterViewSet) # 근태 허용 IP 등록 및 관리 URL


urlpatterns = [
    path("api/", include(router.urls)),  # REST API 등록
]
