# from django.urls import include, path
# from .views import TrainingViewSet, TrainingByUserViewSet
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r"trainings", TrainingViewSet)
# router.register(r"user_and_date", TrainingByUserViewSet)

# urlpatterns = [
#     path("api/", include(router.urls)),  # REST Training ViewSet 등록
#     path("get_today_state/<int:type>_<int:id>_<str:date>/", views.get_training_state), # 당일 훈련일지 작성 상태 api
#     path("get_latest_training/<int:id>_<str:date>/", views.get_latest_training),
# ]
