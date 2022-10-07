from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r"user", UserViewSet) # 유저 계정 리스트 URL
router.register(r"userRegist", UserRegisterViewSet) # 유저 계정 생성 URL

urlpatterns = [
    path("api/", include(router.urls)),
    path("login/", login),  # 로그인 경로
    path("refresh/", TokenRefreshView.as_view()),  # 액세스 토큰 재 발급경로
    path("get_date/", get_server_time),  # 서버시간 가져오기
]