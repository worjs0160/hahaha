# from django.urls import include, path
# from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework import routers  # router import
# from . import views

# from django.views.decorators.csrf import csrf_exempt

# # REST Router 설정
# router = routers.SimpleRouter()  # DefaultRouter 설정
# router.register(r"user", views.UserViewSet)  # UserViewSet 등록
# router.register(r"player", views.PlayerViewSet)  # PlayerViewSet 등록
# router.register(r"coach", views.CoachViewSet)  # CoachViewSet 등록
# # UserRegisterSerializer 등록
# router.register(r"regist", views.UserRegisterViewSet)
# router.register(r"detail", views.DetailViewSet)  # CoachViewSet 등록
# router.register(r"image", views.ImageRegisterViewSet)

# urlpatterns = [
#     path("api/", include(router.urls)),  # REST API 등록
#     path("login/", views.login),  # 로그인 경로
#     path("refresh/", TokenRefreshView.as_view()),  # 액세스 토큰 재 발급경로
#     path("get_date/", views.get_server_time),  # 서버시간 가져오기
#     path("test/", views.test),  # 토큰인증 테스트
#     path("get_matching/<int:team>/", views.get_matching_user),
#     path("authSms/", csrf_exempt(views.AuthSmsView.as_view()))
# ]
