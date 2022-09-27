from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r"category", views.CategoryViewSet) # 메인 카테고리 URL
router.register(r"commondata", views.SubCategoryViewSet) # 서브 카테고리 URL
router.register(r"disability_type", views.DisabilityTypeViewSet) # 장애유형 URL
router.register(r"sport_type", views.SportTypeViewSet) # 운동종목 URL
router.register(r"company_list", views.CompanyListViewSet) # 각 회사 리스트 URL
router.register(r"team_list", views.TeamListViewSet) # 각 훈련기관 리스트 URL

urlpatterns = [
    path("api/", include(router.urls)),
    path("create_sample/", views.create_sample), # 가 데이터 생성 URL
    path("create_company/", views.create_company), # 가 데이터 생성 URL
    path("create_team/", views.create_team)

]
