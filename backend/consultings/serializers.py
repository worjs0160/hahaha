from rest_framework import serializers

from datasets.serializers import *

from .models import *


# 컨설팅 계정용 선수 시리얼라이저
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ['profile']  # 해당 필드를 제외한 모든 필드
        
    def create(self, validatedData):
        user = Player.objects.create(**validatedData)
        user.save()
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["comID"] = CompanyListSerializer(instance.comID).data
        response["sportType"] = SportTypeSerializer(instance.sportType).data
        response["team"] = TeamListSerializer(instance.team).data
        response["disabilityType"] = DisabilityTypeSerializer(instance.disabilityType).data
        response["disabilityGrade"] = SubCategorySerializer(instance.disabilityGrade).data
        response["bloodType"] = SubCategorySerializer(instance.bloodType).data
        response["maritalStatus"] = SubCategorySerializer(instance.maritalStatus).data
        response["militaryService"] = SubCategorySerializer(instance.militaryService).data
        response["education"] = SubCategorySerializer(instance.education).data


        return response

# 선수등록의 이미지 등록 시 사용
class ImageRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "id",
            "name",
            "profile",
        ]