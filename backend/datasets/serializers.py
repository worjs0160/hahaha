import json
import os

from urllib import parse
from urllib import request
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError

from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from users.models import User
from .models import *


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ["id", "name"]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "value", "maincategory"]


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = MainCategory
        fields = [
            "id",
            "name",
            "subcategory",
        ]


# 장애유형 시리얼라이저
class DisabilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisabilityType
        fields = "__all__"


# 운동종목 시리얼라이저
class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = "__all__"


class SportListSerializer(serializers.ListSerializer):
    child = SportTypeSerializer()


# 기업목록 시리얼라이저
class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyList
        fields = "__all__"


# 복지관(훈련기관) 시리얼라이저
class TeamListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamList
        fields = "__all__"



