import re

from rest_framework import serializers
from users.models import User
from .models import *

# 음식사진
class DonateImageSerializer(serializers.ModelSerializer):
    # images = serializers.ImageField(use_url=True)

    class Meta:
        model = donateImage
        fields = "__all__"

# 활동사진
class ActivityImageSerializer(serializers.ModelSerializer):
    # images = serializers.ImageField(use_url=True)

    class Meta:
        model = activityImage
        fields = "__all__"



class userInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "storeName", "storeMaster"]

class DonateInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DonateInfo
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["donator"] = userInfoSerializer(instance.donator).data
        return response

class DonateAndImageInfoSerializer(serializers.ModelSerializer):
    foodImage = DonateImageSerializer(many=True, read_only=True)
    commentImage = ActivityImageSerializer(many=True, read_only=True)

    class Meta:
        model = DonateInfo
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["donator"] = userInfoSerializer(instance.donator).data
        return response

