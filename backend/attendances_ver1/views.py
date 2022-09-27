# import calendar
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.utils.timezone import is_aware
# from django_filters import rest_framework as filters
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, action

# from users.models import User
# from functools import partial

# from .models import Attendance
# from .serializers import *
# from .filters import AttendanceListFilter

# # 모든 유저 뷰셋
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# # Viewset For Attendance List
# class AttendanceViewSet(viewsets.ModelViewSet):
#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer


# # Viewset For Attendance User Containing Attendance List
# class AttendanceListViewSet(viewsets.ModelViewSet):
#     queryset = Attendance.objects.filter(user__is_active=True)
#     serializer_class = AttendanceListSerializer
#     filter_backends = [
#         filters.DjangoFilterBackend,
#     ]
#     filter_class = AttendanceListFilter

#     def get_queryset(self):
#         return super().get_queryset().filter()

#     # attendances/att_list/multiple_delete/
#     # 근태 삭제 시 여러개 삭제
#     @action(methods=["POST"], detail=False)
#     def multiple_delete(self, request, *args, **kwargs):
#         delete_id = request.data
#         if not delete_id:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         for i in delete_id:
#             get_object_or_404(Attendance, pk=int(i)).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     # 선수 퇴근 시간
#     @action(methods=["POST"], detail=False)
#     def todayOffWork(self, request, *args, **kwargs):
#         user = request.data["user"]
#         data = request.data["data"]
#         instance = self.queryset.get(id=user)
#         serializer = self.get_serializer(
#             instance, data=data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)

#     # 근태 생성 시 근무 일 중복 검사
#     def create(self, request, *args, **kwargs):
#         # 근태 생성 시 근무 일 중복 검사
#         try:
#             user_id = request.data['user']
#             date = request.data['startWorkTime'][0:10] 
#             duplicatedAttendance = Attendance.objects.filter(user_id=user_id, startWorkTime__startswith=date).values("startWorkTime")
#             if(date == duplicatedAttendance[0]['startWorkTime'][0:10]):
#                 raise serializers.ValidationError("근태 기록중 같은 날의 기록이 존재합니다.")
#             else:
#                 pass
#         except IndexError:
#             pass
#         return super().create(request)

#     # 근태 수정 시 근무 일 중복 검사
#     def update(self, request, *args, **kwargs):
#         # 근태 수정 시 근무 일 중복 검사
#         try:
#             user_id = request.data['user']
#             date = request.data['startWorkTime'][0:10] 
#             duplicatedAttendance = Attendance.objects.filter(user_id=user_id, startWorkTime__startswith=date).values("startWorkTime")
#             excludedAttendance = duplicatedAttendance.exclude(id=request.data.get('id'))
#             if(date == excludedAttendance[0]['startWorkTime'][0:10]):
#                 raise serializers.ValidationError("근태 기록중 같은 날의 기록이 존재합니다.")
#             else:
#                 pass
#         except IndexError:
#             pass
#         return super().update(request)
    


# # Viewset For Attendance List Containing User Info
# class AttendanceUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(userType=2, is_active=True)
#     serializer_class = AttendanceUserSerializer
#     filter_backends = [
#         filters.DjangoFilterBackend,
#     ]
#     filter_fields = ["id","coach","team","is_active"]


# # 유저 키값, 해당 일로 해당 일부터 7일 간 근무시간 가져오는 함수
# @api_view(["POST"])
# def get_time_week(request, id, date):
#     workTimeList = []

#     for i in range(0, 7):
#         queryset = Attendance.objects.filter(
#             user_id=id, startWorkTime__startswith=date
#         ).values("user", "startWorkTime", "finishWorkTime")

#         try:
#             if (
#                 len(queryset[0]["startWorkTime"]) > 0
#                 and len(queryset[0]["finishWorkTime"]) > 0
#             ):
#                 startWorkTime = queryset[0]["startWorkTime"]
#                 finishWorkTime = queryset[0]["finishWorkTime"]
                
#                 startHour = queryset[0]["startWorkTime"][11:13]
#                 startMin = queryset[0]["startWorkTime"][14:16]
#                 finishHour = queryset[0]["finishWorkTime"][11:13]
#                 finishMin = queryset[0]["finishWorkTime"][14:16]

#                 workHour = int(finishHour) - int(startHour)
#                 workMin = int(finishMin) - int(startMin)

#                 workMin = "0" + str(workMin)
#                 workMin = workMin[-2:]

#                 workTime = f"{workHour}:{workMin}"

#                 code = "1"  # 퇴근 코드
#             elif len(queryset[0]["finishWorkTime"]) == 0:
#                 startWorkTime = queryset[0]["startWorkTime"]
#                 finishWorkTime = None
#                 workTime = None
#                 code = "0"  # 근무중 코드
#         except IndexError:
#             startWorkTime = None
#             finishWorkTime = None
#             workTime = None
#             code = "-1"  # 출근x 코드

#         workTimeList.append(
#             {"date": date, "worktime": workTime, "attendanceState": code, "startWorkTime": startWorkTime, "finishWorkTime": finishWorkTime}
#         )
#         date = str(
#             datetime.datetime.strptime(date, "%Y-%m-%d").date()
#             + datetime.timedelta(days=1)
#         )
#     return JsonResponse(workTimeList, status=200, safe=False)

# # 승인된 계정중에서 type이 3일 때 팀, 1일 때 코치, 4일 때 기업의 소속된 선수 근태 정보 가져오는 함수
# @api_view(["POST"])
# def get_attendance_state(request, type, id, date):
#     if (type == 3):
#         user = User.objects.filter(team=id, userType=2, is_active=True).values("id","username","name")
#     elif (type == 1):
#         user = User.objects.filter(coach=id, userType=2, is_active=True).values("id","username","name")
#     elif (type == 4):
#         user = User.objects.filter(company=id, userType=2, companyPermission=True).values("id","username","name")
#     else:
#         return JsonResponse({"msg": "올바르지 않은 타입입니다."}, status=200, safe=False)

#     workInfo = []
    
#     if (len(user) != 0): # 유저 유무 확인
#         for i in range(len(user)):
#             attendance_list = Attendance.objects.filter(user_id=user[i]['id'] ,startWorkTime__startswith=date).values("user", "startWorkTime", "finishWorkTime")
#             try:
#                 if (len(attendance_list[0]["startWorkTime"]) > 0 and len(attendance_list[0]["finishWorkTime"]) > 0):
#                     code = "1" # 퇴근 코드
#                     workDay = date
#                     player = user[i]['name']
#                     startTime = attendance_list[0]["startWorkTime"][11:16]
#                     finishTime = attendance_list[0]["finishWorkTime"][11:16]
#                 elif len(attendance_list[0]["finishWorkTime"]) == 0:
#                     code = "0"  # 근무중 코드
#                     workDay = date
#                     player = user[i]['name']
#                     startTime = attendance_list[0]["startWorkTime"][11:16]
#                     finishTime = attendance_list[0]["finishWorkTime"][11:16]
#             except:
#                 code = "-1"  # 출근x 코드
#                 workDay = date
#                 player = user[i]['name']
#                 startTime = None
#                 finishTime = None
#             workInfo.append({ "user": player, "date": workDay, "state": code, "startTime": startTime, "finishTime": finishTime})
#         return JsonResponse(workInfo, status=200, safe=False)
#     else:
#         return JsonResponse({"msg": "소속된 선수가 존재하지 않습니다."}, status=200, safe=False)

# # 유저 키값과 년, 월, 일 입력하여 근태 정보 가져오는 함수
# @api_view(["POST"])
# def get_attendance(request, id, date):
#     workTimeList = []
#     queryset = Attendance.objects.filter(user_id=id, startWorkTime__startswith=date).values("user", "startWorkTime", "finishWorkTime")

#     if(len(date) == 10): # 해당 일에 대한 근태 기록
#         try:
#             # 출근/퇴근이 모두 존재
#             if (
#                 len(queryset[0]["startWorkTime"]) > 0
#                 and len(queryset[0]["finishWorkTime"]) > 0
#             ):
#                 start_hour = queryset[0]["startWorkTime"][11:13]
#                 start_min = queryset[0]["startWorkTime"][14:16]
#                 finish_hour = queryset[0]["finishWorkTime"][11:13]
#                 finish_min = queryset[0]["finishWorkTime"][14:16]

#                 workHour = int(finish_hour) - int(start_hour)
#                 workMin = int(finish_min) - int(start_min)

#                 workMin = "0" + str(workMin)
#                 workMin = workMin[-2:]

#                 workTime = f"{workHour}:{workMin}"

#                 code = "1"  # 근무완료
#                 return JsonResponse(
#                     {
#                         "date": date,
#                         "worktime": workTime,
#                         "startWorkTime": queryset[0]["startWorkTime"],
#                         "finishWorkTime": queryset[0]["finishWorkTime"],
#                         "attendanceState": code,
#                     }
#                 )
#             # 출근 O / 퇴근 X
#             elif len(queryset[0]["finishWorkTime"]) == 0:
#                 code = "0"  # 근무중
#                 return JsonResponse(
#                     {
#                         "date": date,
#                         "worktime": None,
#                         "startWorkTime": queryset[0]["startWorkTime"],
#                         "finishWorkTime": queryset[0]["finishWorkTime"],
#                         "attendanceState": code,
#                     }
#                 )
#         except IndexError:
#             code = "-1"  # 출근 X
#             return JsonResponse(
#                 {
#                     "date": date,
#                     "worktime": None,
#                     "startWorkTime": None,
#                     "finishWorkTime": None,
#                     "attendanceState": code,
#                 }
#             )
#     elif (len(date) == 7): # 해당 월에 대한 근태 기록
#         year = date[0:4]
#         month = date[5:7]
#         firstDay = "-01"
#         date = date + firstDay
#         monthlength = calendar.monthrange(int(year), int(month))
#         workTimeList = []

#         for i in range((monthlength[1])):
#             queryset = Attendance.objects.filter(
#                 user_id=id, startWorkTime__startswith=date
#             ).values("user", "startWorkTime", "finishWorkTime")
#             try:
#                 if (
#                     len(queryset[0]["startWorkTime"]) > 0
#                     and len(queryset[0]["finishWorkTime"]) > 0
#                 ):
#                     startHour = queryset[0]["startWorkTime"][11:13]
#                     startMin = queryset[0]["startWorkTime"][14:16]
#                     finishHour = queryset[0]["finishWorkTime"][11:13]
#                     finishMin = queryset[0]["finishWorkTime"][14:16]

#                     workHour = int(finishHour) - int(startHour)
#                     workMin = int(finishMin) - int(startMin)

#                     workMin = "0" + str(workMin)
#                     workMin = workMin[-2:]

#                     workTime = f"{workHour}:{workMin}"
#                     startTime = queryset[0]["startWorkTime"]
#                     finishTime = queryset[0]["finishWorkTime"]
#                     code = "1"  # 퇴근 코드
#                 elif len(queryset[0]["finishWorkTime"]) == 0:
#                     workTime = None
#                     startTime = queryset[0]["startWorkTime"]
#                     finishTime = None
#                     code = "0"  # 근무중 코드

#             except IndexError:
#                 workTime = None
#                 startTime = None
#                 finishTime = None
#                 code = "-1"  # 출근x 코드

#             workTimeList.append(
#                 {"date": date, "worktime": workTime, "startWorkTime": startTime, "finishWorkTime": finishTime, "attendanceState": code}
#             )
#             date = str(
#                 datetime.datetime.strptime(date, "%Y-%m-%d").date()
#                 + datetime.timedelta(days=1)
#             )
#         return JsonResponse(workTimeList, status=200, safe=False)

#     elif (len(date) == 4): # 해당 연도에 대한 근태 기록
#         year = date[0:4]
#         month = date[5:7]
#         firstDate = "-01-01"
#         date = date + firstDate
#         workTimeList = []

#         for i in range(365):
#             queryset = Attendance.objects.filter(
#                 user_id=id, startWorkTime__startswith=date
#             ).values("user", "startWorkTime", "finishWorkTime")
#             try:
#                 if (
#                     len(queryset[0]["startWorkTime"]) > 0
#                     and len(queryset[0]["finishWorkTime"]) > 0
#                 ):
#                     startHour = queryset[0]["startWorkTime"][11:13]
#                     startMin = queryset[0]["startWorkTime"][14:16]
#                     finishHour = queryset[0]["finishWorkTime"][11:13]
#                     finishMin = queryset[0]["finishWorkTime"][14:16]

#                     workHour = int(finishHour) - int(startHour)
#                     workMin = int(finishMin) - int(startMin)

#                     workMin = "0" + str(workMin)
#                     workMin = workMin[-2:]

#                     workTime = f"{workHour}:{workMin}"
#                     startTime = queryset[0]["startWorkTime"]
#                     finishTime = queryset[0]["finishWorkTime"]
#                     code = "1"  # 퇴근 코드
#                 elif len(queryset[0]["finishWorkTime"]) == 0:
#                     workTime = None
#                     startTime = queryset[0]["startWorkTime"]
#                     finishTime = None
#                     code = "0"  # 근무중 코드

#             except IndexError:
#                 workTime = None
#                 startTime = None
#                 finishTime = None
#                 code = "-1"  # 출근x 코드

#             workTimeList.append(
#                 {"date": date, "worktime": workTime, "startWorkTime": startTime, "finishWorkTime": finishTime, "attendanceState": code}
#             )
#             date = str(
#                 datetime.datetime.strptime(date, "%Y-%m-%d").date()
#                 + datetime.timedelta(days=1)
#             )
#         return JsonResponse(workTimeList, status=200, safe=False)
#     else:
#         return JsonResponse({"msg": "날짜를 다시 입력해주세요."}, status=400, safe=False)