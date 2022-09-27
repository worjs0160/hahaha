# REST위한 Serializer.py 생성
from rest_framework import serializers
from .models import Attendance  # 선언한 모델 import
from users.models import User
from datasets.serializers import *
import datetime


# # 근태관리용 전체 유저 시리얼라이저
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "name", "userType", "team", "company", "coach", "sportType"]


# # 선수의 근태 정보 및 근태 상태 시리얼라이저
# class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
#     attendanceState = serializers.SerializerMethodField()

#     class Meta:
#         model = Attendance
#         fields = (
#             "user",
#             "startWorkTime",
#             "finishWorkTime",
#             "workPlace",
#             "memo",
#             "attendanceState",
#         )  # 직렬화할 필드 설정

#     # 근태 상태 검증
#     def get_attendanceState(self, obj):
#         try:
#             data = 0
#             if len(obj.finishWorkTime) > 1:
#                 data = 1
#         except:
#             data = None
#         return data

# # 선수들의 근태 리스트 및 해당 리스트의 선수 정보 포함 시리얼라이저
# class AttendanceListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Attendance
#         fields = [
#             "url",
#             "id",
#             "user",
#             "startWorkTime",
#             "finishWorkTime",
#             "workPlace",
#             "memo",
#         ]  # 직렬화할 필드 설정

#     # 근태 정보에 해당하는 유저 포함하여 직렬화
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         response["user"] = UserSerializer(instance.user).data
#         return response

#     # 근무 일 중복 검사 및 출근시간, 퇴근시간 알맞은 형식 검증
#     def validate(self, value):
#         try:
#             datetime.datetime.strptime(value['startWorkTime'], '%Y-%m-%d %H:%M:%S')
#             if len(value['finishWorkTime']) > 1: # 퇴근시간이 입력됐을 경우 검증
#                 if (value['startWorkTime'][0:10] == value['finishWorkTime'][0:10]): # 출근 일자, 퇴근 일자 같음
#                     try:
#                         datetime.datetime.strptime(value['finishWorkTime'], '%Y-%m-%d %H:%M:%S')
#                         return value
#                     except ValueError:
#                         raise serializers.ValidationError("퇴근시간을 정확히 입력하세요.")
#                 else:
#                     raise serializers.ValidationError("출근일과 퇴근일이 다를 수 없습니다.") # 출근 시간, 퇴근 시간 검증
#             return value

#         except ValueError:
#             raise serializers.ValidationError("출근시간을 정확히 입력하세요.")
        

# # 근태관리 유저 카드 디테일에 들어갈 내용 시리얼라이저
# class AttendanceUserSerializer(serializers.ModelSerializer):
#     attendances = AttendanceSerializer(many=True, read_only=True)
#     coachName = serializers.SerializerMethodField()

#     team = TeamListSerializer()
#     company = CompanyListSerializer()
#     sportType = SportTypeSerializer()
#     disabilityType = DisabilityTypeSerializer()
#     disabilityGrade = SubCategorySerializer()
#     bloodType = SubCategorySerializer()

#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "username",
#             "name",
#             "phoneNum",
#             "email",
#             "weight",
#             "height",
#             "wheelchair",
#             "userType",
#             "coach",
#             "coachName",
#             "career",
#             "guardianName",
#             "guardianNum",
#             "profileImgSrc",
#             "attendances",
#             "company",
#             "team",
#             "sportType",
#             "disabilityType",
#             "disabilityGrade",
#             "bloodType",
#         ]

#     # 해당 선수의 코치 이름을 가져오는 함수
#     def get_coachName(self, obj):
#         try:
#             coachName = User.objects.filter(id=obj.coach).values("name")
#         except:
#             coachName = None
#         return coachName
