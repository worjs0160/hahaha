# from django.db.models.query import QuerySet
# from attendances.models import Attendance
# from django.http.response import JsonResponse
# from django_filters import rest_framework as filters
# from rest_framework import viewsets
# from .models import Training
# from .filters import TrainingByUserFilter
# from .serializers import TrainingSerializer
# from rest_framework.decorators import api_view
# from users.models import User

# ## findAll, findByDate, findById findByCoach findByUser


# class TrainingViewSet(viewsets.ModelViewSet):
#     queryset = Training.objects.all()
#     serializer_class = TrainingSerializer


# class TrainingByUserViewSet(viewsets.ModelViewSet):
#     queryset = Training.objects.all()
#     serializer_class = TrainingSerializer
#     filter_backends = [
#         filters.DjangoFilterBackend,
#     ]
#     filter_class = TrainingByUserFilter


# # 소속 선수 미작성된 훈련일지 개수 가져오기
# @api_view(["GET"])
# def count_unwritten_training(request, team):
#     pass

# # type별로
# # 1일때 코치의 소속된 선수,
# # 2일땐 선수 자신의,
# # 3일땐 복지관 소속의 선수,
# # 4일땐 기업 소속의 선수의 훈련일지 정보 가져오는 함수
# @api_view(["POST"])
# def get_training_state(request, type, id, date):
#     if (type == 3):
#         user = User.objects.filter(team=id, userType=2, is_active=True).values("id", "name")
#     elif (type == 2):
#         user = User.objects.filter(id=id, userType=2, is_active=True).values("id", "name")
#     elif (type == 1):
#         user = User.objects.filter(coach=id, userType=2, is_active=True).values("id", "name")
#     elif (type == 4):
#         user = User.objects.filter(company=id, userType=2, companyPermission=True).values("id", "name")
#     else:
#         return JsonResponse({"msg": "올바르지 않은 타입입니다."}, status=200, safe=False)

#     trainingDataList = []

#     if (len(user) != 0):
#         for i in range(len(user)):
#             todayAttendance = Attendance.objects.filter(user=user[i]["id"], startWorkTime__startswith=date).values("startWorkTime")
#             if (len(todayAttendance) != 0):
#                 todayTraining = Training.objects.filter(user=user[i]["id"], trainingDate=date).values("user", "contents")
#                 if(len(todayTraining) != 0):
#                     userName = user[i]["name"]
#                     trainingState = "1" # 훈련일지 작성 완료
#                     contents = todayTraining[0]["contents"]
#                 else:
#                     userName = user[i]["name"]
#                     trainingState = "-1" # 훈련일지 작성 중, 아직 근무 중
#                     contents = None
#             else:
#                 userName = user[i]["name"]
#                 trainingState = "0" # 미작성
#                 contents = None
#             trainingDataList.append(
#                 {"name": userName, "state": trainingState, "contents": contents}
#             )

#         return JsonResponse(trainingDataList, status=200, safe=False)
#     else:
#         return JsonResponse({"msg": "해당 소속의 선수가 존재하지 않습니다."})


# # 선수 해당 월의 훈련일지 가져오기
# @api_view(["POST"])
# def get_latest_training(request, id, date):
#     trainingData = Training.objects.filter(user_id=id, trainingDate__startswith=date).values("user", "trainingDate", "contents")
#     trainingData = sorted(trainingData, key=lambda e: (e['trainingDate'])) # 근무일지의 순서를 날짜 기준으로 정렬
#     result = []
#     if (len(trainingData) > 0):
#         try:
#             for index in range(31):
#                 username = User.objects.get(id=trainingData[index]["user"]).name
#                 trainingDate = trainingData[index]["trainingDate"]
#                 trainingContents = trainingData[index]["contents"]
#                 result.append({"name": username, "date":trainingDate, "contents": trainingContents})
#             return JsonResponse(result, status=200, safe=False)
#         except IndexError:
#             return JsonResponse(result, status=200, safe=False)
#     else:
#          return JsonResponse({"msg": "해당 선수의 훈련일지가 존재하지 않습니다."}, status=400)