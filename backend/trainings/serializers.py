from calendar import week
from rest_framework import serializers

from .models import *
from users.models import *
from users.serializers import *
from attendances.serializers import *


class TrainingImageSerializer(serializers.ModelSerializer):
    # images = serializers.ImageField(use_url=True)

    class Meta:
        model = TrainingImage
        fields = ('id', 'images','width','height')

class TrainingSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    # 해당 일의 요일을 가져오는 함수
    def get_day(self, obj):
        try:
            day = obj.workDate.weekday()
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

    class Meta:
        model = Training
        fields = "__all__"

# 유저 트레이닝 데이터에서 사용할 용도
class CCTrainingSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    # 이미지 정보 포함하여 직렬화
    images = TrainingImageSerializer(many=True, read_only=True)

    # 해당 일의 요일을 가져오는 함수
    def get_day(self, obj):
        try:
            day = obj.workDate.weekday()
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


    class Meta:
        model = Training
        fields = "__all__"


class TrainingUserSerializer(serializers.ModelSerializer):
    trainings = CCTrainingSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["attType"] = AttTypeSerializer(instance.attType).data
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
            "trainings",
            "attType",
        ]

