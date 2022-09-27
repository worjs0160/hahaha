from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r"user", UserViewSet) # 이용자 계정 리스트 URL
router.register(r"employee", EmployeeViewSet) # 근로자 계정 리스트 URL
router.register(r"userRegist", UserRegisterViewSet) # 이용자 계정 생성 URL
router.register(r"empRegist", EmployeeRegisterViewSet) # 근로자 계정 생성 URL
router.register(r"image", ImageRegisterViewSet) # 계정 내 프로필 추가 URL

urlpatterns = [
    path("api/", include(router.urls)),
    path("login/", login),  # 로그인 경로
    path("refresh/", TokenRefreshView.as_view()),  # 액세스 토큰 재 발급경로
    path("get_date/", get_server_time),  # 서버시간 가져오기
    path("getIP/", getIP)
]
