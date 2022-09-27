
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from datasets.models import *
from .models import *
from .serializers import *


import random
from datetime import date, timedelta 
import calendar 
import string
import time

# 컨설팅 계정용 뷰셋
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["comID"]

# 회원가입시 프로필 이미지 담당 뷰셋
class ImageRegisterViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = ImageRegisterSerializer

# 가 데이터(컨설팅 유저) 생성
def create_random_user(request):
    for i in range(10): # 숫자 조절하여 원하는 만큼 생성
        
        # 이름 설정
        firstNameSample = "김이박최정강조윤장임"
        middleNameSample = "민서예지도하주윤채현지"
        lastNameSample = "준윤우원호후서연아은진"

        randName = ""
        randName += random.choice(firstNameSample)
        randName += random.choice(middleNameSample)
        randName += random.choice(lastNameSample)

        # 나이, 생년월일 설정
        randYear = random.randint(1973, 2013)
        randMonth = random.randint(1, 12)
        randDay = random.randint(1, calendar.monthrange(randYear, randMonth)[1])
        randBirthDate = str(randYear).ljust(4, "0") + str(randMonth).rjust(2, "0") + str(randDay).rjust(2, "0")

        randAge = 2023 - randYear

        # 성별 설정
        randGender = str(time.time())[-2:]
        if int(randGender)%2 == 1:
            randGender = '남자'
        else:
            randGender = '여자'

        # 전화번호 설정
        randPhone = '010' + str(int(random.random() * 100000000))

        # 주소 설정

        cityList = ['서울특별시', '부산광역시', '인천광역시', '대구광역시', '대전광역시', '광주광역시', '울산광역시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '세종특별자치시']
        districtList = [['종로구', '중구', '용산구', '성동구', '광진구'],
                    ['중구', '서구', '동구', '영도구', '부산진구'],
                    ['중구', '동구', '서구', '남구', '북구'],
                    ['중구', '동구', '미추홀구', '연수구', '남동구'],
                    ['동구', '서구', '남구', '북구', '광산구'],
                    ['동구', '중구', '서구', '유성구', '대덕구'],
                    ['중구', '남구', '동구', '북구', '울주군'],
                    ['수원시', '고양시', '용인시', '성남시', '부천시'],
                    ['춘천시', '원주시', '강릉시', '동해시', '태백시'],
                    ['청주시', '충주시', '제천시', '보은군', '옥천군'],
                    ['천안시', '공주시', '보령시', '아산시', '서산시'],
                    ['전주시', '군산시', '익산시', '정읍시', '남원시'],
                    ['목포시', '여수시', '순천시', '나주시', '광양시'],
                    ['포항시', '경주시', '김천시', '안동시', '구미시'],
                    ['창원시', '진주시', '통영시', '사천시', '김해시'],
                    ['제주시', '서귀포시'],
                    ['']
        ]

        randCityIndex = random.randint(0, 16)
        city = cityList[randCityIndex]

        if randCityIndex < 15:
            randDistrctIndex = random.randint(0, 4)
            district = districtList[randCityIndex][randDistrctIndex]
        elif randCityIndex == 15:
            randDistrctIndex = random.randint(0, 1)
            district = districtList[randCityIndex][randDistrctIndex]
        else:
            district = ''
        
        addr = city + " " + district

        # 보호자 이름 설정
        randGuardianName = ""
        randGuardianName += random.choice(firstNameSample)
        randGuardianName += random.choice(middleNameSample)
        randGuardianName += random.choice(lastNameSample)

        # 보호자 연락처 설정
        randGuardianPhone = '010' + str(int(random.random() * 100000000))

        # 운동종목 설정
        randSportType = random.randint(1, 13)
        sportType = SportType.objects.get(id=randSportType)

        # 경력 설정
        if randAge < 14:
            randCareer = random.randint(1, 3) # 초
        elif randAge < 17:
            randCareer = random.randint(1, 5) # 중
        elif randAge < 20:
            randCareer = random.randint(1, 7) # 고
        elif randAge < 25:
            randCareer = random.randint(1, 10)
        else:
            randCareer = random.randint(1, 15) 

        # 장애유형 설정
        randDisabilityType = random.randint(1, 6)
        disabilityType = DisabilityType.objects.get(id=randDisabilityType)

        # 장애등급 설정
        randDisabilityGrade = random.randint(1, 2)
        disabilityGrade = SubCategory.objects.get(id=randDisabilityGrade)

        # 신장 설정
        randHeight = random.randint(150, 190)

        # 체중 설정
        randWeight = random.randint(60, 100)

        # 최종학력 설정
        if randAge < 14:
            randEducation = 12 # 초
        elif randAge < 17:
            randEducation = random.randint(12, 13) # 중
        elif randAge < 20: 
            randEducation = random.randint(12, 14) # 고
        elif randAge < 25:
            randEducation = random.randint(12, 15) 
        else:
            randEducation = random.randint(12, 18) 
        
        education = SubCategory.objects.get(id=randEducation)
        # 학교명 설정

        # 가데이터(유저) 생성
        Player.objects.create(name=randName, age=randAge, gender=randGender, phone=randPhone, birthDate=randBirthDate, userAddr1=addr, sportType=sportType, career=randCareer, disabilityType=disabilityType, disabilityGrade=disabilityGrade, height=randHeight, weight=randWeight, education=education, guardianName=randGuardianName, guardianNum=randGuardianPhone)

    return HttpResponse("샘플 데이터 입력")