import re

from rest_framework import serializers
from .models import *

class DonateInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DonateInfo
        fields = "__all__"


# 기부 음식 이미지 등록 시 사용
class ImageRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateInfo
        fields = [
            "id",
            "foodName",
            "foodImage",
        ]