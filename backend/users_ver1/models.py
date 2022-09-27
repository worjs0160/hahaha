# from django.core.validators import MinLengthValidator
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils import timezone

# from core.models import TimeStampedModel
# from .utils import make_signature

# from datetime import datetime
# import json, requests, time, random, datetime

# # 아바타 이미지 경로 제작 함수
# def avatar_path(instance):
#     return instance.username + "/" + "profile_img"


# class User(AbstractUser):
#     # 기본 정보
#     username = models.CharField(verbose_name="아이디", validators=[MinLengthValidator(5)], max_length=20, unique=True)
#     name = models.CharField(verbose_name="이름", max_length=10, null=True, default=None) 
#     birthDate = models.CharField(verbose_name="생년월일", max_length=8, null=True, default=None)
#     gender = models.CharField(verbose_name="성별", max_length=2, null=True, default=None)
#     profileImgSrc = models.ImageField(
#         verbose_name="프로필 이미지", upload_to="user/profile", default="user/profile/basicProfile.jpg"
#     )
#     phoneNum = models.CharField(
#         verbose_name="전화번호", max_length=11, null=True, default=None
#     )
#     userZip = models.CharField(verbose_name="우편번호", max_length=10, null=True, default=None)
#     userAddr1 = models.CharField(verbose_name="기본주소", max_length=50, null=True, default=None)
#     userAddr2 = models.CharField(verbose_name="상세주소", max_length=30, null=True, default=None)
#     userType = models.IntegerField(
#         verbose_name="계정유형(1-코치, 2-선수, 3-복지관, 4-기관계정, 5-영업사원)", null=True, default=None
#     )
#     coach = models.IntegerField(verbose_name="담당코치", null=True, default=None)

#     # 경력사항
#     sportType = models.ForeignKey(
#         "datasets.SportType",
#         on_delete=models.SET_NULL,
#         verbose_name="운동종목",
#         null=True, default=None,
#     )
#     team = models.ForeignKey(
#         "datasets.TeamList",
#         on_delete=models.SET_NULL,
#         verbose_name="소속 복지관",
#         null=True, default=None,
#     )
#     company = models.ForeignKey(
#         "datasets.CompanyList",
#         on_delete=models.SET_NULL,
#         verbose_name="소속 회사",
#         null=True, default=None
#     )
#     career = models.IntegerField(verbose_name="선수경력", null=True, default=None)
#     awards = models.CharField(verbose_name="수상경력", max_length=100, null=True, default=None)

#     # 개인사항
#     disabilityType = models.ForeignKey(
#         "datasets.DisabilityType",
#         on_delete=models.SET_NULL,
#         verbose_name="장애유형",
#         related_name="disability_type",
#         null=True, default=None,
#     )
#     disabilityGrade = models.ForeignKey(
#         "datasets.SubCategory",
#         on_delete=models.SET_NULL,
#         verbose_name="중증/경증",
#         limit_choices_to={"maincategory": 1},
#         related_name="disability_grade",
#         null=True, default=None
#     )
#     height = models.CharField(verbose_name="신장", max_length=10, null=True, default=None)
#     weight = models.CharField(verbose_name="체중", max_length=10, null=True, default=None)
#     bloodType = models.ForeignKey(
#         "datasets.SubCategory",
#         on_delete=models.SET_NULL,
#         verbose_name="혈액형",
#         limit_choices_to={"maincategory": 2},
#         null=True, default=None
#     )
#     wheelchair = models.BooleanField(verbose_name="휠체어", default=False)
#     eyesightL = models.CharField(
#         verbose_name="시력(좌)", max_length=5, null=True, default=None
#     )
#     eyesightR = models.CharField(
#         verbose_name="시력(우)", max_length=5, null=True, default=None
#     )
#     maritalStatus = models.ForeignKey(
#         "datasets.SubCategory",
#         on_delete=models.SET_NULL,
#         verbose_name="결혼여부",
#         limit_choices_to={"maincategory": 3},
#         related_name="marital_status",
#         null=True, default=None
#     )
#     militaryService = models.ForeignKey(
#         "datasets.SubCategory",
#         on_delete=models.SET_NULL,
#         verbose_name="병역여부",
#         limit_choices_to={"maincategory": 4},
#         related_name="military_service",
#         null=True, default=None
#     )
#     education = models.ForeignKey(
#         "datasets.SubCategory",
#         on_delete=models.SET_NULL,
#         verbose_name="최종학력",
#         limit_choices_to={"maincategory": 5},
#         related_name="education",
#         null=True, default=None
#     )
#     school = models.CharField(verbose_name="학교명", max_length=20, null=True, default=None)
#     department = models.CharField(verbose_name="학과명", max_length=20, null=True, default=None)
    
#     monthWorkTime = models.CharField(verbose_name="월 근무시간", max_length=20, null=True, default=None)
#     workDay = models.ManyToManyField("datasets.SubCategory", verbose_name="근무요일", related_name="users", null=True, default=None)
#     trainingStartTime = models.CharField(verbose_name="훈련시작시간", max_length=20, null=True, default=None)
#     trainingFinishTime = models.CharField(verbose_name="훈련종료시간", max_length=20, null=True, default=None)
#     companyPermission = models.BooleanField(verbose_name="기업승인", default=False)

#     # 기관 정보
#     divisionName = models.CharField(verbose_name="부서명", max_length=20, null=True, default=None)
#     divisionNum = models.CharField(verbose_name="직통번호", max_length=20, null=True, default=None)
    
#     # 보호자 정보
#     guardianName = models.CharField(
#         verbose_name="보호자 이름(1)", max_length=20, null=True, default=None
#     )
#     relation = models.CharField(
#         verbose_name="선수와의 관계(1)", max_length=10, null=True, default=None
#     )
#     guardianNum = models.CharField(
#         verbose_name="보호자 전화번호(1)", max_length=20, null=True, default=None
#     )
#     guardianEmail = models.EmailField(
#         verbose_name="보호자 이메일(1)", max_length=20, null=True, default=None
#     )
#     subGuardianName = models.CharField(
#         verbose_name="보호자 이름(2)", max_length=20, null=True, default=None
#     )
#     subRelation = models.CharField(
#         verbose_name="선수와의 관계(2)", max_length=10, null=True, default=None
#     )
#     subGuardianNum = models.CharField(
#         verbose_name="보호자 전화번호(2)", max_length=20, null=True, default=None
#     )
#     subGuardianEmail = models.EmailField(
#         verbose_name="보호자 이메일(2)", max_length=20, null=True, default=None
#     )
    
#     class Meta:
#         verbose_name = "유저"
#         verbose_name_plural = "유저"


# class AuthSms(TimeStampedModel):
#     phoneNum = models.CharField(verbose_name='휴대폰 번호', primary_key=True, max_length=11)
#     authNum = models.IntegerField(verbose_name='인증 번호')
    
#     class Meta:
#         db_table = 'SMS 인증 테이블1'
#         verbose_name = "SMS 인증 테이블2"
#         verbose_name_plural = "SMS 인증 테이블3"

#     def save(self, *args, **kwargs):
#         self.authNum = random.randint(1000, 10000)
#         super().save(*args, **kwargs)
#         self.send_sms() # 인증번호가 담긴 SMS를 전송

#     def send_sms(self):
#         timestamp = str(int(time.time() * 1000))
#         headers = {
#             'Content-Type': "application/json; charset=UTF-8", # 네이버 참고서 차용
#             'x-ncp-apigw-timestamp': timestamp, # 네이버 API 서버와 5분이상 시간차이 발생시 오류
#             'x-ncp-iam-access-key': 'c7yFrVbmdKDGOdI9qSZJ', #(예시 = 'nCH86JcJ6FCl40eYc4qp')
#             'x-ncp-apigw-signature-v2': make_signature(timestamp) # utils.py 이용
#         }
#         body = {
#             "type": "SMS", 
#             "contentType": "COMM",
#             "from": "01063806257", # 사전에 등록해놓은 발신용 번호 입력, 타 번호 입력시 오류
#             "content": "[테스트] 인증 번호 [{}]를 입력해주세요.".format(self.authNum), # 메세지를 이쁘게 꾸며보자
#             "messages": [{"to": f"{self.phoneNum}"}] # 네이버 양식에 따른 messages.to 입력
#         }
#         body = json.dumps(body)
        
#         requests.post("https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:270940729584:weplay/messages", headers=headers, data=body)
#         # 발송 URI 부분에는 아래 URL을 넣어주면 된다.
#         # https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:270940729584:weplay/messages 
#         # 다만, 너무 길고 동시에 보안이슈가 있기에 별도로 분기해놓은 settings 파일에 넣어서 불러오는 것을 추천한다.

#     @classmethod
#     def check_authNum(cls, p_num, c_num):
#         time_limit = timezone.now() - datetime.timedelta(minutes=5)
#         result = cls.objects.filter(
#             phoneNum=p_num,
#             authNum=c_num,
#             modifiedTime__gte=time_limit
#         )
#         if result:
#             return True
#         return False