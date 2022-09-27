from datetime import datetime
from rest_framework import serializers

from .models import *
from users.models import *
from datasets.models import *
from users.serializers import *


# 근태관리용 전체 유저 시리얼라이저
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "profile", "teamID", "comID", "name", "username"]


class AttTypeSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()


    # 근무 유형의 요일리스트를 가져오는 함수
    def get_days(self, obj):
        result = []
        key = str(obj.id)
        if key and key != 'N':
            day_list = AttendanceType.objects.filter(id=key).values('workDay')
            for n in day_list:
                day = list(SubCategory.objects.filter(
                    id=n['workDay']).values('value'))
                for item in day:
                    result.append(item['value'][0:1])

            return result
        else:
            return result

    class Meta:
        model = AttendanceType
        fields = "__all__"


# 근태 유형을 포함한 근태 기록 직렬화
class AttendanceSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    days = serializers.SerializerMethodField()

    # 근무 유형의 요일리스트를 가져오는 함수
    def get_days(self, obj):
        result = []
        key = str(obj.attType.id)
        if key and key != 'N':
            day_list = AttendanceType.objects.filter(id=key).values('workDay')
            for n in day_list:
                day = list(SubCategory.objects.filter(
                    id=n['workDay']).values('value'))
                for item in day:
                    result.append(item['value'][0:1])

            return result
        else:
            return result

    # 해당 일의 요일을 가져오는 함수
    def get_day(self, obj):
        try:
            day = obj.onTime.weekday()
            if day == 0:
                result = "월"
            elif day == 1:
                result = "화"
            elif day == 2:
                result = "수"
            elif day == 3:
                result = "목"
            elif day == 4:
                result = "금"
            elif day == 5:
                result = "토"
            elif day == 6:
                result = "일"
            else:
                result = None
            return result
        except:
            return None

    # 근태 정보에 해당하는 근태 유형을 포함
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["attType"] = AttTypeSerializer(instance.attType).data
        response["user"] = EmployeeSerializer(instance.user).data
        return response

    class Meta:
        model = Attendance
        fields = "__all__"


# 근무 기록, 유형을 포함한 사용자 직렬화
class AttendanceUserSerializer(serializers.ModelSerializer):
    # 외래키로 받아온 데이터를 필터링해서 가져오기
    attendances = AttendanceSerializer(many=True, read_only=True)
    attType = serializers.SerializerMethodField()
    
    
    # 근무 유형의 요일리스트를 가져오는 함수
    def get_attType(self, obj):
        days = []
        result = {}
        key = str(obj.attType.id)

        if key and key != 'N':
            day_list = AttendanceType.objects.filter(id=key).values('workDay')
            monthWorkTime = list(AttendanceType.objects.filter(id=key).values('monthWorkTime'))[0]['monthWorkTime']
            onTime = list(AttendanceType.objects.filter(id=key).values('onTime'))[0]['onTime']
            offTime = list(AttendanceType.objects.filter(id=key).values('offTime'))[0]['offTime']
            time1 = datetime.strptime(onTime,"%H:%M")
            time2 = datetime.strptime(offTime,"%H:%M")
            timeInterval = float(str(time2 - time1).split(':')[0] + '.' + str(time2 - time1).split(':')[1])
            
            for n in day_list:
                day = list(SubCategory.objects.filter(
                    id=n['workDay']).values('value'))
                for item in day:
                    days.append(item['value'][0:1])
            result = {
                "days": days,
                "monthWorkTime": monthWorkTime,
                "timeInterval": timeInterval,
                "onTime": onTime,
                "offTime": offTime,
            }
            return result
        else:
            return result
        return None

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "userType",
            "profile",
            "comID",
            "attendances",
            "attType",
        ]


class AttTypeUserSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()

    # 근무 유형의 요일을 가져오는 함수
    def get_days(self, obj):
        result = []
        key = obj.attType.id
        if key and key != 'N':
            day_list = AttendanceType.objects.filter(id=key).values('workDay')
            for n in day_list:
                day = list(SubCategory.objects.filter(
                    id=n['workDay']).values('value'))
                for item in day:
                    result.append(item['value'][0:1])
            return result
        else:
            return result

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["attType"] = AttTypeSerializer(instance.attType).data
        # response["user"] = EmployeeSerializer(instance.user).data
        return response

    class Meta:
        model = Employee
        fields = [
            "id",
            "username",
            "name",
            "userType",
            "profile",
            "comID",
            "attType",
            "days"
        ]


# 근태 허용 IP 테이블 시리얼라이저
class IPRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = IPRegister
        fields = "__all__"
