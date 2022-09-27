# import re
# from datetime import datetime
# from functools import partial
# from django.db.models import Q
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt  # csrf 회피용 (테스트)
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import update_last_login
# from django_filters import rest_framework as filters  # 장고 필터 추가
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import (
#     permission_classes,
#     authentication_classes,
#     api_view,
#     action,
# )
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser  # JSON파서 임포트
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken  # 토큰 발행 위한 라이브러리
# from rest_framework import viewsets, status
# from .serializers import (
#     ImageRegisterSerializer,
#     UserRegisterSerializer,
#     UserSerializer,
#     UserDetailSerializer,
# )
# from .models import AuthSms, User
# from datasets.models import SubCategory, TeamList, CompanyList

# import json, requests, time, random
# # Django
# from django.views import View
# from .utils import make_signature
# from django.utils import timezone

# # 토큰 발급 함수
# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         "refresh_token": str(refresh),
#         "access_token": str(refresh.access_token),
#     }


# # 서버시간 가져오는 함수
# @csrf_exempt
# def get_server_time(request):
#     if request.method == "GET":
#         now = datetime.now()
#         return JsonResponse({"date": now}, status=200)


# @api_view(["POST"])
# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)  # 데이터 JSON으로 파싱
#         inputId = data["username"]
#         inputPw = data["password"]

#         if not inputId or not inputPw:
#             return JsonResponse({"msg": "아이디와 비밀번호을 모두 입력해주세요"}, status=400)

#         try:
#             # DB에서 이름으로 유저 검색
#             obj = User.objects.get(username=inputId)

#             if obj.is_active is False:
#                 return JsonResponse({"msg": "활성화되지 않은 유저입니다."}, status=401)

#             # 장고 유저인증 사용하여 인증(성공시 id 반환, 실패시 None 반환)
#             loginRes = authenticate(username=inputId, password=inputPw)

#             if loginRes:
#                 # JWT 토큰 생성
#                 tokens = get_tokens_for_user(loginRes)
#                 # print(loginRes.id)
#                 update_last_login(None, loginRes)  # 마지막 로그인 시간 업데이트

#                 # 프론트 서버로 보낼 데이터 정의
#                 reqData = {
#                     "msg": "로그인 성공",
#                     "user_id": loginRes.id,
#                 }
#                 reqData["tokens"] = tokens  # 반환 데이터 딕셔너리 병합
#                 return JsonResponse(reqData, status=200)
#             else:
#                 return JsonResponse({"msg": "비밀번호가 틀렸습니다."}, status=401)

#         except User.DoesNotExist:
#             return JsonResponse({"msg": "유저가 존재하지 않습니다."}, status=400)


# @api_view(["POST"])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JWTAuthentication,))
# @csrf_exempt
# def test(request):
#     if request.method == "POST":
#         return HttpResponse("성공", status=200)


# # ModelViewSet은 기본적으로 Create, Retrieve, Update, Partial_Update, Destroy, List 를 지원한다.
# # 반복되는 로직을 하나의 클래스로 결합할 수 있음 -> queryset 을 단 한번만 정의하면 됨, ModelViewSet 활용->Router를 사용함으로써, URL설정을 다룰 필요가 없음
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     # /users/api/user/new_users/
#     @action(detail=False, methods=["get"])
#     def new_users(self, request):
#         qs = self.queryset.filter(
#             Q(userType=1) | Q(userType=2), is_active=False)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)


# # 같은 팀 소속의 선수 불러오기
# class PlayerViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(userType=2)
#     serializer_class = UserSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ["id", "team", "company", "coach", "is_active", "companyPermission"]

#     @action(detail=False, methods=["get"])
#     def null_players(self, request):
#         team = request.GET.get("team")
#         qs = self.queryset.filter(coach=None)
#         if team is not None:
#             qs = self.queryset.filter(Q(coach=None) | Q(coach=-1), team=team)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=["post"])
#     def set_players(self, request):
#         list_player = request.data["list_player"]
#         set_data = request.data["set_data"]

#         for player in list_player:
#             instance = self.queryset.get(id=player["id"])
#             serializer = self.get_serializer(
#                 instance, data=set_data, partial=partial)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)

#     # 활성화 여부에 따른 선수 검색 기능
#     @action(detail=False, methods=["get"])
#     def players_matching(self, request):
#         team = request.GET.get("team")
#         qs = self.queryset.filter(coach=None)

#         if team is not None:
#             qs = self.queryset.filter(is_active=True, team=team, coach=None)
#         else:
#             return Response({"msg": "소속 복지관이 없습니다."}, status=400)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=["post"])
#     def set_active_players(self, request):
#         list_player = request.data["list_player"]
#         set_data = request.data["set_data"]

#         for player in list_player:
#             instance = self.queryset.get(id=player["id"])
#             serializer = self.get_serializer(
#                 instance, data=set_data, partial=partial)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)

#     @action(detail=False, methods=["post"])
#     def set_company_permission_players(self, request):
#         list_player = request.data["list_player"]
#         set_data = request.data["set_data"]

#         for player in list_player:
#             instance = self.queryset.get(id=player["id"])
#             serializer = self.get_serializer(
#                 instance, data=set_data, partial=partial)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)


# class CoachViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.filter(userType=1)
#     serializer_class = UserSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filter_fields = ["team", "coach"]

#     # 활성화 여부에 따른 코치 검색 기능
#     # @action(detail=False, methods=["get"])
#     # def false_coaches(self, request):
#     #     team = request.GET.get("team")

#     #     if team is not None:
#     #         qs = self.queryset.filter(is_active=False, team=team)
#     #     else:
#     #         return Response({"msg": "소속 복지관이 없습니다."}, status=400)
#     #     serializer = self.get_serializer(qs, many=True)
#     #     return Response(serializer.data)

#     @action(detail=False, methods=["get"])
#     def coaches_player(self, request):
#         team = request.GET.get("team")

#         if team is not None:
#             qs = self.queryset.filter(is_active=True, team=team)
#         else:
#             return Response({"msg": "소속 복지관이 없습니다."}, status=400)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     @action(detail=False, methods=["post"])
#     def set_active_coaches(self, request):
#         list_player = request.data["list_player"]
#         set_data = request.data["set_data"]

#         for player in list_player:
#             instance = self.queryset.get(id=player["id"])
#             serializer = self.get_serializer(
#                 instance, data=set_data, partial=partial)
#             serializer.is_valid(raise_exception=True)
#             self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)


# # 유저 회원가입, 정보수정 담당 뷰셋
# class UserRegisterViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = [AllowAny]  # 해당 뷰셋 접근권한 설정
#     filter_backends = [
#         filters.DjangoFilterBackend,
#     ]
#     filter_fields = ["name","guardianNum"]

#     # users/api/regist/chk_username/
#     @action(detail=False, methods=["post"])
#     def chk_username(self, request):
#         try:
#             if not request.data["username"]:
#                 return Response({"msg": "아이디를 입력해주세요"}, status=406)

#             if not re.match("^[a-zA-Z0-9_]*$", request.data["username"]):
#                 return Response({"msg": "아이디는 영문과 숫자로만 이루어져야 합니다."}, status=406)

#             obj = User.objects.get(username=request.data["username"])
#             return Response({"msg": "사용중인 id 입니다."}, status=406)
#         except User.DoesNotExist:
#             return Response({"msg": "사용 가능한 id 입니다."}, status=200)

#     # 아이디 찾기 위한 함수, users/api/regist/find_id/
#     @action(detail=False, methods=["post"])
#     def find_id(self, request):
#         if not request.data["name"] or not request.data["guardianNum"]:
#             return Response({"msg": "값을 모두 입력해주세요."}, status=400)

#         try:
#             user = User.objects.get(
#                 name=request.data["name"], guardianNum=request.data["guardianNum"]
#             )
#             return Response({"username": user.username}, status=200)

#         except User.DoesNotExist:
#             return Response({"msg": "해당하는 유저가 존재하지 않습니다."}, status=400)

#     # 비밀번호 찾기에서 유저정보 검증 함수, users/api/regist/val_info/
#     @action(detail=False, methods=["post"])
#     def val_info(self, request):
#         try:
#             obj = User.objects.get(**(request.data))
#             return Response({"msg": "해당하는 유저가 존재합니다.", "id": obj.id}, status=200)

#         except User.DoesNotExist:
#             return Response({"msg": "해당하는 유저가 존재하지 않습니다."}, status=406)


# # 회원가입시 프로필 이미지 담당 뷰셋
# class ImageRegisterViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = ImageRegisterSerializer


# class DetailViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     permission_classes = [AllowAny]  # AllowAny(Default) 무조건 view 호출 허용, 해당 뷰셋 접근권한 설정 

#     # 활성화 여부에 따른 선수 검색 기능
#     @action(detail=False, methods=["get"])
#     def detail_search(self, request):
#         team = request.GET.get("team")

#         if team is not None:
#             qs = self.queryset.filter(team=team, userType=2)
#         else:
#             return Response({"msg": "소속 복지관이 없습니다."}, status=400)
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

#     # 인원관리 미 배정 선수 코치 및 계약 설정
#     @action(detail=False, methods=["post"])
#     def set_player_contect(self, request):
#         player = request.data["player"]
#         set_data = request.data["set_data"]
#         # 카테고리 데이터 저장
#         category_data = request.data["category_data"]

#         # 선수의 카테고리 데이터를 수정하기 위해서 가져옴
#         player_data = User.objects.get(pk=player)

#         # 주간 근무 데이터
#         weekDayList = []
#         for week in category_data["workDay"]:
#             # 선택한 인덱스의 주간 정보를 가져오는 작업
#             weekData = SubCategory.objects.filter(
#                 maincategory=7).values()[week]
#             # 선택한 인덱스의 주간 정보를 쿼리셋으로 선택하는 작업
#             appendWeekData = SubCategory.objects.filter(
#                 maincategory=7, id=weekData['id'])

#             weekDayList.append(appendWeekData)

#         for idx, val in enumerate(weekDayList):

#             if idx > 0:
#                 weekDayList[0] = weekDayList[0].union(weekDayList[idx])
#         player_data.workDay.set(weekDayList[0])
#         # player_data.save()

#         instance = self.queryset.get(id=player)
#         serializer = self.get_serializer(
#             instance, data=set_data, partial=partial)

#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)
        
#     # 인원관리 상세정보 수정
#     @action(detail=False, methods=["post"])
#     def set_detail_player(self, request):
#         player = request.data["player"]
#         set_data = request.data["set_data"]
#         # 카테고리 데이터 저장
#         category_data = request.data["category_data"]

#         # 선수의 카테고리 데이터를 수정하기 위해서 가져옴
#         player_data = User.objects.get(pk=player)
#         # 서브 카테고리 조회 (maincategory=1 장애등급)
#         disability_grade = SubCategory.objects.get(
#             maincategory=1, id=category_data["disabilityGrade"])

#         # 서브 카테고리 데이터 선수 데이터에 저장
#         player_data.disabilityGrade = disability_grade
#         player_data.save()
#         instance = self.queryset.get(id=player)
#         serializer = self.get_serializer(
#             instance, data=set_data, partial=partial)

#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response({"msg": "성공"}, status=200)

#     # 회원정보 수정 함수, users/api/detail/update_info/
#     @action(methods=["post"], detail=False)
#     def update_info(self, request, *args, **kwargs):
#         user = request.data["user"]
#         data = request.data["data"]

#         # 카테고리 데이터 저장
#         category_data = request.data["category_data"]

#         # 선수의 카테고리 데이터를 수정하기 위해서 가져옴
#         player_data = User.objects.get(pk=user)
#         # 서브 카테고리 조회 (maincategory=1 장애등급)
#         team = TeamList.objects.get(id=category_data["team"])

#         company = CompanyList.objects.get(id=category_data["company"])

#         # 서브 카테고리 데이터 선수 데이터에 저장
#         player_data.team = team
#         player_data.company = company
#         player_data.save()
        
#         instance = self.queryset.get(id=user)
#         serializer = self.get_serializer(
#             instance, data=data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({"msg": "성공"}, status=200)


# class NewUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# @api_view(["POST"])
# def get_matching_user(request, team):
#     coachQueryset = User.objects.filter(
#         userType=1, team=team).values("id", "name", "email")
#     TeamName = TeamList.objects.filter(id=team).values("value")
#     userList = []

#     try:
#         for coach in coachQueryset:
#             userList.append([{**coach, **TeamName[0]}])
#             playerData = User.objects.filter(
#                 userType=2, team=team, coach=coach["id"]).values("name", "coach", "team", "id", "email")

#             for key in range(len(userList)):
#                 for player in playerData:
#                     if userList[key][0]["id"] == player["coach"] and player["coach"] >= 0:
#                         userList[key].append({**player, **TeamName[0]})
#     except IndexError:
#         return JsonResponse({"msg": "훈련기관 내에 코치가 존재하지않습니다."}, status=400)

#     return JsonResponse({"data": userList}, status=200)

# # 네이버 SMS 인증
# class AuthSmsView(APIView):
#     def post(self, request):
#         lenNumber = 11 # 휴대폰 번호 길이
#         try:
#             p_num = request.data['phoneNum']
#             if len(p_num) != lenNumber:
#                 return JsonResponse({"messege": "11자리 휴대폰 번호를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
#         except KeyError:
#             return Response({'message': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             AuthSms.objects.update_or_create(phoneNum=p_num)
#         return Response({'message': '성공적으로 SMS 인증번호가 발송되었습니다.'})

#     def get(self, request):
#         try:
#             p_num = request.query_params['phoneNum']
#             a_num = request.query_params['authNum']
#         except KeyError:
#             return Response({'message': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             result = AuthSms.check_authNum(p_num, a_num)
#             if result == True:
#                 pass
#         return Response({'message': '성공', 'result': result})