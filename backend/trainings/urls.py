from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r"trainings", TrainingViewSet) # 전체 근무일지 리스트 URL
router.register(r"userTrainings", TrainingUserViewSet) # 근로자와 근무일지 리스트 URL
router.register(r"userTrainingsImg", CreateImageViewSet)  # 유저기반 훈련일지 URL
router.register(r"CCUserTrainings", CCTrainingViewSet)  # 이미지 조회용 훈련일지 URL


urlpatterns = [
    path("api/", include(router.urls)),
]