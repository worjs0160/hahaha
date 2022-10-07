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
from .filters import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]  # 해당 뷰셋 접근권한 설정
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    filter_fields = ["name"]

    # users/api/regist/chk_username/
    @action(detail=False, methods=["post"])
    def chk_username(self, request):
        try:
            if not request.data["username"]:
                return Response({"msg": "아이디를 입력해주세요"}, status=406)

            if not re.match("^[a-zA-Z0-9_]*$", request.data["username"]):
                return Response({"msg": "아이디는 영문과 숫자로만 이루어져야 합니다."}, status=406)

            obj = User.objects.get(username=request.data["username"])
            return Response({"msg": "사용중인 id 입니다."}, status=406)
        except User.DoesNotExist:
            return Response({"msg": "사용 가능한 id 입니다."}, status=200)

    # 아이디 찾기 위한 함수, users/api/regist/find_id/
    @action(detail=False, methods=["post"])
    def find_id(self, request):
        if not request.data["name"] or not request.data["guardianNum"]:
            return Response({"msg": "값을 모두 입력해주세요."}, status=400)

        try:
            user = User.objects.get(
                name=request.data["name"], guardianNum=request.data["guardianNum"]
            )
            return Response({"username": user.username}, status=200)

        except User.DoesNotExist:
            return Response({"msg": "해당하는 유저가 존재하지 않습니다."}, status=400)

    # 비밀번호 찾기에서 유저정보 검증 함수, users/api/regist/val_info/
    @action(detail=False, methods=["post"])
    def val_info(self, request):
        try:
            obj = User.objects.get(**(request.data))
            return Response({"msg": "해당하는 유저가 존재합니다.", "id": obj.id}, status=200)

        except User.DoesNotExist:
            return Response({"msg": "해당하는 유저가 존재하지 않습니다."}, status=406)


# 토큰 발급 함수
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh_token": str(refresh),
        "access_token": str(refresh.access_token),
    }


# 서버시간 가져오는 함수
@csrf_exempt
def get_server_time(request):
    if request.method == "GET":
        now = datetime.now()
        return JsonResponse({"date": now}, status=200)


# 로그인 함수
@api_view(["POST"])
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)  # 데이터 JSON으로 파싱
        inputId = data["username"]
        inputPw = data["password"]

        if not inputId or not inputPw:
            return JsonResponse({"msg": "아이디와 비밀번호을 모두 입력해주세요"}, status=400)

        try:
            # DB에서 이름으로 유저 검색
            obj = User.objects.get(username=inputId)

            if obj.is_active is False:
                return JsonResponse({"msg": "활성화되지 않은 유저입니다."}, status=401)

            # 장고 유저인증 사용하여 인증(성공시 id 반환, 실패시 None 반환)
            loginRes = authenticate(username=inputId, password=inputPw)

            if loginRes:
                # JWT 토큰 생성
                tokens = get_tokens_for_user(loginRes)
                # print(loginRes.id)
                update_last_login(None, loginRes)  # 마지막 로그인 시간 업데이트

                # 프론트 서버로 보낼 데이터 정의
                reqData = {
                    "msg": "로그인 성공",
                    "user_id": loginRes.id,
                }
                reqData["tokens"] = tokens  # 반환 데이터 딕셔너리 병합
                return JsonResponse(reqData, status=200)
            else:
                return JsonResponse({"msg": "비밀번호가 틀렸습니다."}, status=401)

        except User.DoesNotExist:
            return JsonResponse({"msg": "유저가 존재하지 않습니다."}, status=400)
