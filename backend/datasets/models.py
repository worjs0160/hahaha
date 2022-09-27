import json
import os

from django.db import models

from urllib import parse
from urllib import request
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import HTTPError


# 공통코드 모델 작성 (주)
class MainCategory(models.Model):
    id = models.IntegerField(verbose_name="상위코드", primary_key=True)
    name = models.CharField(verbose_name="주 카테고리명", max_length=50, unique=True)

    class Meta:
        verbose_name = "공통코드 카테고리"
        verbose_name_plural = "공통코드 카테고리"

    def __str__(self):
        return self.name


# 공통코드 모델 작성 (부)
class SubCategory(models.Model):
    id = models.IntegerField(verbose_name="하위코드", primary_key=True)
    maincategory = models.ForeignKey(
        "MainCategory",
        on_delete=models.CASCADE,
        related_name="subcategory",
        verbose_name="주 카테고리명",
    )
    value = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "공통코드 데이터"
        verbose_name_plural = "공통코드 데이터"

    def __str__(self):
        return f"{self.maincategory.name}/{self.value}"


# 장애유형 테이블
class DisabilityType(models.Model):
    id = models.IntegerField(verbose_name="장애코드", primary_key=True)
    value = models.CharField(verbose_name="장애유형", max_length=50)

    class Meta:
        verbose_name = "장애유형"
        verbose_name_plural = "장애유형"

    def __str__(self):
        return self.value


# 운동종목 테이블
class SportType(models.Model):
    id = models.IntegerField(verbose_name="종목코드", primary_key=True)
    value = models.CharField(verbose_name="운동종목", max_length=50)

    class Meta:
        verbose_name = "운동종목"
        verbose_name_plural = "운동종목"

    def __str__(self):
        return self.value


# 기업목록 테이블
class CompanyList(models.Model):
    id = models.IntegerField(verbose_name="기업코드", primary_key=True)
    comName = models.CharField(verbose_name="기업명", max_length=50)
    ceoName = models.CharField(verbose_name="대표자명", max_length=50, null=True, blank=True)
    businessNum = models.CharField(verbose_name="사업자등록번호", max_length=50, null=True, blank=True)
    comZip = models.CharField(verbose_name="우편번호", max_length=50, null=True, blank=True)
    comAddr1 = models.CharField(verbose_name="기본주소", max_length=50, null=True, blank=True)
    comAddr2 = models.CharField(verbose_name="상세주소", max_length=100, null=True, blank=True)
    logoPath = models.CharField(verbose_name="로고 경로", max_length=50, null=True, blank=True)
    openDate = models.CharField(verbose_name="설립일", max_length=50, null=True, blank=True)
    comNum = models.CharField(verbose_name="회사 대표 전화번호", max_length=50, null=True, blank=True)
    managerName = models.CharField(verbose_name="담당자 이름", max_length=50, null=True, blank=True)
    managerNum = models.CharField(verbose_name="담당자 전화번호", max_length=50, null=True, blank=True)
    introduction = models.CharField(verbose_name="회사 소개", max_length=100, null=True, blank=True)
    latitude = models.CharField(verbose_name="위도", max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="경도", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "기업목록"
        verbose_name_plural = "기업목록"

    def save(self, *args, **kwargs):
        print(self.comAddr1)
        try:
            comAddr = self.comAddr1
            add_urlenc = parse.quote(comAddr) # 아스키코드 형식이 아닌 글자를 URL 인코딩
            url = os.environ.get("naver_geocoding_url") + add_urlenc
            request_url = Request(url)
            request_url.add_header('X-NCP-APIGW-API-KEY-ID', os.environ.get("naver_client_ID"))
            request_url.add_header('X-NCP-APIGW-API-KEY', os.environ.get("naver_client_PW"))
            try:
                response = urlopen(request_url) # URL에 해당하는 Response Instance를 Return
            except HTTPError as e:
                print('HTTP Error!')
                latitude = None
                longitude = None
            else:
                rescode = response.getcode() # status code 리턴
                if rescode == 200:
                    response_body = response.read().decode('utf-8') # utf-8: 유니코드를 위한 가변 길이 문자 인코딩 방식
                    response_body = json.loads(response_body) # json 형식으로 주소 Return
                    if response_body['addresses'] == [] :
                        print("'result' not exist!")
                        latitude = None
                        longitude = None
                    else:
                        latitude = response_body['addresses'][0]['y'] # 경도
                        longitude = response_body['addresses'][0]['x'] # 위도
                        print("Success!")
                else:
                    print('Response error code : %d' % rescode)
                    latitude = None
                    longitude = None
        except:
            latitude = None
            longitude = None
        
        self.latitude = latitude
        self.longitude = longitude
        super().save(*args, **kwargs)
            
    def __str__(self):
        return self.comName


# 복지관(훈련기관)목록 테이블
class TeamList(models.Model):
    id = models.IntegerField(verbose_name="복지관(훈련기관) 코드", primary_key=True)
    teamName = models.CharField(verbose_name="복지관(훈련기관)명", max_length=50)
    teamZip = models.CharField(verbose_name="우편번호", max_length=50, null=True, blank=True)
    teamAddr1 = models.CharField(verbose_name="기본주소", max_length=50, null=True, blank=True)
    teamAddr2 = models.CharField(verbose_name="상세주소", max_length=100, null=True, blank=True)
    teamNum = models.CharField(verbose_name="복지관(훈련기관) 대표 전화번호", max_length=50, null=True, blank=True)
    logoPath = models.CharField(verbose_name="로고 경로", max_length=50, null=True, blank=True)
    allowedIP = models.CharField(verbose_name="허용된 아이피", max_length=100, null=True, blank=True)
    latitude = models.CharField(verbose_name="위도", max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="경도", max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "복지관(훈련기관)목록"
        verbose_name_plural = "복지관(훈련기관)목록"

    def save(self, *args, **kwargs):
        print(self.teamAddr1)
        try:
            teamAddr = self.teamAddr1
            add_urlenc = parse.quote(teamAddr) # 아스키코드 형식이 아닌 글자를 URL 인코딩
            url = os.environ.get("naver_geocoding_url") + add_urlenc
            request_url = Request(url)
            request_url.add_header('X-NCP-APIGW-API-KEY-ID', os.environ.get("naver_client_ID"))
            request_url.add_header('X-NCP-APIGW-API-KEY', os.environ.get("naver_client_PW"))
            try:
                response = urlopen(request_url) # URL에 해당하는 Response Instance를 Return
            except HTTPError as e:
                print('HTTP Error!')
                latitude = None
                longitude = None
            else:
                rescode = response.getcode() # status code 리턴
                if rescode == 200:
                    response_body = response.read().decode('utf-8') # utf-8: 유니코드를 위한 가변 길이 문자 인코딩 방식
                    response_body = json.loads(response_body) # json 형식으로 주소 Return
                    if response_body['addresses'] == [] :
                        print("'result' not exist!")
                        latitude = None
                        longitude = None
                    else:
                        latitude = response_body['addresses'][0]['y'] # 경도
                        longitude = response_body['addresses'][0]['x'] # 위도
                        print("Success!")
                else:
                    print('Response error code : %d' % rescode)
                    latitude = None
                    longitude = None
        except:
            latitude = None
            longitude = None
        
        self.latitude = latitude
        self.longitude = longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return self.teamName
