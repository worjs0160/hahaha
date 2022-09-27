from django.urls import path, include

from rest_framework import routers

from .views import *


# REST Router 설정
router = routers.SimpleRouter()
router.register(r"approval", ApprovalViewSet)
router.register(r"monthly", MonthlyReportViewSet)
router.register(r"competition", CompetitionReportViewSet)
router.register(r"vacation", VacationReportViewSet)

urlpatterns = [
    path("api/", include(router.urls)),  # REST API 등록
]
