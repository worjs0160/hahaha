import re

from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


# 이용자 회원가입 및 정보 수정 전용
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value):
        passwordValid = self.context["request"].data["passwordValid"]
        res = custom_validate_password(value, passwordValid)
        if res != 0:
            raise serializers.ValidationError(res)
        return value

    def create(self, validatedData):
        user = User.objects.create_user(**validatedData)
        user.set_password(validatedData["password"])
        user.is_active = True
        user.save()
        return user

    def update(self, instance, validatedData):
        # 검증 데이터에 패스워드 있는지 확인
        if "password" in validatedData:
            instance.set_password(validatedData["password"])
            instance.save()

        return instance


# 비밀번호 검사 함수
def custom_validate_password(password, passwordValid):
    # 특수문자 종류 정의
    specialChar = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*",
                    "(", ")", ",", "<", ".", ">", "/", "?", "[", "]", "{", "}", ]
    if not password or not passwordValid:
        return "패스워드와 패스워드 확인을 입력해주세요."
    elif password != passwordValid:
        return "패스워드와 패스워드 확인이 일치하지 않습니다."
    # 패스워드 길이가 7자리보다 짧습니다.
    elif len(password) < 7:
        return "패스워드 길이가 7자리보다 짧습니다."
    # 패스워드는 최소 1개 이상의 숫자가 포함되어야 합니다.
    elif re.search("[0-9]+", password) is None:
        return "패스워드는 최소 1개 이상의 숫자가 포함되어야 합니다."
    # 패스워드는 최소 1개 이상의 영문 대소문자가 포함되어야 합니다.
    elif re.search("[a-z]+", password) is None and re.search("[A-Z]+", password) is None:
        return "패스워드는 최소 1개 이상의 영문 대문자나 소문자가 포함되어야 합니다."
    # 패스워드는 최소 1개 이상의 특수문자가 포함되어야 합니다.
    # any()는 iterable 객체를 인수로 받고, 인수중 하나라도 참이 있으면 True반환
    # elif not any(c in specialChar for c in password):
    #     return "패스워드는 최소 1개 이상의 특수문자가 포함되어야 합니다."
    else:
        return 0