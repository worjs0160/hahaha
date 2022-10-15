from urllib.request import urlopen

from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt  # csrf 회피용 (테스트)
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django_filters import rest_framework as filters  # 장고 필터 추가

from rest_framework import viewsets
from rest_framework.decorators import permission_classes, authentication_classes, api_view, action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken  # 토큰 발행 위한 라이브러리
from rest_framework.parsers import JSONParser, MultiPartParser  # JSON파서 임포트
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *
from .filters import *

# 사진정보를 id로 포함한 데이터 담당 뷰셋(주로 기부내용에 이미지를 저장할때 사용)
class DonateInfoViewSet(viewsets.ModelViewSet):
    queryset = DonateInfo.objects.all()
    serializer_class = DonateInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["donator"]

# 사진정보 포함한 데이터 담당 뷰셋(주로 이미지 url까지 조회할때 사용)
class DonateAndImageInfoViewSet(viewsets.ModelViewSet):
    queryset = DonateInfo.objects.all()
    serializer_class = DonateAndImageInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["donator"]

# 음식 사진 등록 담당 뷰셋
class FoodImageViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = donateImage.objects.all()
    serializer_class = DonateImageSerializer
    filter_class = FoodImageFilter

# 활동 사진 등록 담당 뷰셋
class ActivityImageViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = activityImage.objects.all()
    serializer_class = ActivityImageSerializer
    filter_class = ActivityImageFilter