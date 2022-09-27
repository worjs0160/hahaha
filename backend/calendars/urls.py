from django.urls import URLPattern, path, include

from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r"calendar", CalendarViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]