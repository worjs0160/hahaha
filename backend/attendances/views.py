import datetime
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response


from .serializers import *
from .filters import *


# 근무자 전용 근태 정보 뷰셋
class EmpAttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AttendanceFilter

    # 근태 생성 시 근무 일 중복 검사
    def create(self, request, *args, **kwargs):
        try:
            userID = request.data['user']
            # 0000-00-00T00:00:00 슬라이싱 0000-00-00
            date = str(datetime.strptime(request.data['onTime'][0:10], "%Y-%m-%d"))[0:10]
            duplicatedAttendance = Attendance.objects.filter(
                user_id=userID, onTime__startswith=date[0:10])  # 중복되는 근태 기록 가져오기
            if(len(duplicatedAttendance) >= 1):  # 같은 날짜의 근태 기록 존재 유무 확인
                raise serializers.ValidationError("근태 기록중 같은 날의 기록이 존재합니다.")
            else:
                pass
        except IndexError:
            pass
        return super().create(request)

    # def get_queryset(self):
    #     return super().get_queryset().filter()


# 고용기업 전용 근태 정보 뷰셋
class ComAttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AttendanceFilter

    # 근태 생성 시 근무 일 중복 검사
    def create(self, request, *args, **kwargs):
        try:
            userID = request.data['user']
            # 0000-00-00T00:00:00 슬라이싱 0000-00-00
            date = str(datetime.datetime.strptime(
                request.data['onTime'][0:10], "%Y-%m-%d"))[0:10]
            duplicatedAttendance = Attendance.objects.filter(
                user_id=userID, onTime__startswith=date[0:10])  # 중복되는 근태 기록 가져오기
            if(len(duplicatedAttendance) >= 1):  # 같은 날짜의 근태 기록 존재 유무 확인
                raise serializers.ValidationError("근태 기록중 같은 날의 기록이 존재합니다.")
            else:
                pass
        except IndexError:
            pass
        return super().create(request)

    # 근태 수정 시 근무 일 중복 검사 함수
    def update(self, request, *args, **kwargs):
        try:
            userID = request.data['user']
            # 0000-00-00T00:00:00 슬라이싱 0000-00-00
            date = str(datetime.datetime.strptime(
                request.data['onTime'][0:10], "%Y-%m-%d"))[0:10]
            duplicatedAtt = Attendance.objects.filter(
                user_id=userID, onTime__startswith=date[0:10])  # 중복되는 근태 기록 가져오기
            excludedAtt = duplicatedAtt.exclude(
                id=request.data.get('id'))  # 수정하는 근태 기록은 제외 한 나머지 근태 중복 검사
            if(len(excludedAtt) >= 1):
                raise serializers.ValidationError("근태 기록중 같은 날의 기록이 존재합니다.")
            else:
                pass
        except IndexError:
            pass
        return super().update(request)

    # 근태 삭제 시 다중 삭제 함수
    @action(methods=["DELETE"], detail=False)
    def multiple_delete(self, request, *args, **kwargs):
        try:
            deleteID = request.data
            if not deleteID:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for i in deleteID:
                get_object_or_404(Attendance, pk=int(i)).delete()
        except IndexError:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


# 근태 유형 뷰셋
class AttTypeViewSet(viewsets.ModelViewSet):
    queryset = AttendanceType.objects.all()
    serializer_class = AttTypeSerializer


class AttendanceUserViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter()
    serializer_class = AttendanceUserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = UserAttFilter


# Viewset For AttType List Containing User Info
class AttTypeUserViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter()
    serializer_class = AttTypeUserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "comID", "userType"]


# 근태 허용 IP 관리 뷰셋
class IPRegisterViewSet(viewsets.ModelViewSet):
    queryset = IPRegister.objects.all()
    serializer_class = IPRegisterSerializer
