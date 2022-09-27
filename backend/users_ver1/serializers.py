# # 입력받은 데이터의 유효성 검사위한 Serializer.py
# import re  # 문자열 검색위한 re 라이브러리 임포트
# from django.contrib.auth import authenticate, get_user_model, models
# from django.http.response import HttpResponse
# from rest_framework import serializers  # rest serializer 임포트
# from .models import User  # 선언한 모델 import
# from datasets.serializers import *


# # 비밀번호 검사 함수
# def custom_validate_password(password, passwordValid):
#     # 특수문자 종류 정의
#     specialChar = [
#         "~",
#         "`",
#         "!",
#         "@",
#         "#",
#         "$",
#         "%",
#         "^",
#         "&",
#         "*",
#         "(",
#         ")",
#         ",",
#         "<",
#         ".",
#         ">",
#         "/",
#         "?",
#         "[",
#         "]",
#         "{",
#         "}",
#     ]
#     if not password or not passwordValid:
#         return "패스워드와 패스워드 확인을 입력해주세요."
#     elif password != passwordValid:
#         return "패스워드와 패스워드 확인이 일치하지 않습니다."
#     # 패스워드 길이가 7자리보다 짧습니다.
#     elif len(password) < 7:
#         return "패스워드 길이가 7자리보다 짧습니다."
#     # 패스워드는 최소 1개 이상의 숫자가 포함되어야 합니다.
#     elif re.search("[0-9]+", password) is None:
#         return "패스워드는 최소 1개 이상의 숫자가 포함되어야 합니다."
#     # 패스워드는 최소 1개 이상의 영문 대소문자가 포함되어야 합니다.
#     # elif re.search("[a-z]+", password) is None or re.search("[A-Z]+", password) is None:
#     #     return "패스워드는 최소 1개 이상의 영문 대문자와 소문자가 포함되어야 합니다."
#     # 패스워드는 최소 1개 이상의 특수문자가 포함되어야 합니다.
#     # any()는 iterable 객체를 인수로 받고, 인수중 하나라도 참이 있으면 True반환
#     elif not any(c in specialChar for c in password):
#         return "패스워드는 최소 1개 이상의 특수문자가 포함되어야 합니다."
#     else:
#         return 0


# # ModelSerializer 클래스를 사용하면 Model에 정의한 필드에 해당하는 값을 Serializer 에서 사용할 수 있다.
# class UserSerializer(serializers.ModelSerializer):
#     team = TeamListSerializer()
#     company = CompanyListSerializer()
#     sportType = SportTypeSerializer()
#     disabilityType = DisabilityTypeSerializer()
#     disabilityGrade = SubCategorySerializer()
#     bloodType = SubCategorySerializer()
#     workDay = SubCategorySerializer(many=True)

#     class Meta:
#         model = User
#         # 직렬화할 필드 설정
#         fields = [
#             "id",
#             "username",
#             "name",
#             "email",
#             "userType",
#             "coach",
#             "phoneNum",
#             "profileImgSrc",
#             "team",
#             "company",
#             # 부가정보
#             "sportType",
#             "disabilityType",
#             "disabilityGrade",
#             "bloodType",
#             "guardianNum",
#             "guardianName",
#             "height",
#             "weight",
#             "is_active",
#             "monthWorkTime",
#             "workDay",
#             "trainingStartTime",
#             "trainingFinishTime",
#             "companyPermission",
#         ]

# # 회원가입 전용
# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         exclude = ['profileImgSrc'] # 해당 필드를 제외한 모든 필드


#     def validate_password(self, value):
#         passwordValid = self.context["request"].data["passwordValid"]
#         res = custom_validate_password(value, passwordValid)
#         if res != 0:
#             raise serializers.ValidationError(res)
#         return value

#     def create(self, validatedData):
#         user = User.objects.create_user(**validatedData)
#         user.set_password(validatedData["password"])
#         user.is_active = True
#         user.save()
#         return user

#     def update(self, instance, validatedData):
#         # 검증 데이터에 패스워드 있는지 확인
#         if "password" in validatedData:
#             instance.set_password(validatedData["password"])
#             instance.save()

#         return instance


# # 회원가입 이미지 등록 시 사용
# class ImageRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = [
#             "id",
#             "name",
#             "profileImgSrc",
#         ]


# # 유저의 정보 제공시 사용
# class UserDetailSerializer(serializers.ModelSerializer):
#     team = TeamListSerializer()
#     company = CompanyListSerializer()
#     sportType = SportTypeSerializer()
#     disabilityType = DisabilityTypeSerializer()
#     disabilityGrade = SubCategorySerializer()
#     bloodType = SubCategorySerializer()
#     workDay = SubCategorySerializer(many=True)

#     class Meta:
#         model = User
#         # 직렬화할 필드 설정
#         fields = [
#             "id",
#             "username",
#             "coach",
#             "name",
#             "birthDate",
#             "phoneNum",
#             "disabilityType",
#             "disabilityGrade",
#             "height",
#             "weight",
#             "bloodType",
#             "wheelchair",
#             "guardianName",
#             "guardianNum",
#             "team",
#             "company",
#             "sportType",
#             "monthWorkTime",
#             "workDay",
#             "trainingStartTime",
#             "trainingFinishTime",
#         ]
