# from django.urls import path, include
# from rest_framework import routers
# from . import views

# # REST Router 설정
# router = routers.SimpleRouter() # DefaultRouter 설정
# router.register(r"att", views.AttendanceViewSet) # 근태 정보 API
# router.register(r"user", views.UserViewSet) # 근태관리용 유저 API 
# router.register(r"att_list", views.AttendanceListViewSet) # 근태 정보 안에 선수 정보 포함한 API
# router.register(r"att_user", views.AttendanceUserViewSet) # 선수 정보 안에 모든 근태 정보 포함한 API

# urlpatterns = [
#     path("api/", include(router.urls)), # REST API 등록
#     path("work_time_week/<int:id>_<str:date>/", views.get_time_week), # 해당 일 기준 일주일 치 근무시간 가져오기
#     path("get_today_state/<int:type>_<int:id>_<str:date>/", views.get_attendance_state), # 해당 일 기준 소속된 팀의 근태 상태 가져오기
#     path("get_work_time/<int:id>_<str:date>/", views.get_attendance), # 해당 년, 월, 일로 선수의 근태 데이터 가져오기
# ]
