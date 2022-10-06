import re

from datetime import datetime
from functools import partial
from urllib.request import urlopen

from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt  # csrf 회피용 (테스트)
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as filters  # 장고 필터 추가

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, authentication_classes, api_view, action
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken  # 토큰 발행 위한 라이브러리
from rest_framework.parsers import JSONParser  # JSON파서 임포트

from .serializers import *
from .models import *

class DonateInfoViewSet(viewsets.ModelViewSet):
    queryset = DonateInfo.objects.all()
    serializer_class = DonateInfoSerializer


# 음식 사진 등록 담당 뷰셋
class ImageRegisterViewSet(viewsets.ModelViewSet):
    queryset = DonateInfo.objects.all()
    serializer_class = ImageRegisterSerializer