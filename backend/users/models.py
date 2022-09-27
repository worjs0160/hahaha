from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import UserTimeStampedModel, TimeStampedModel

import os


# class Profile(TimeStampedModel):
#     width = models.CharField(verbose_name="이미지 너비",
#                              blank=True, null=True, max_length=10)
#     height = models.CharField(verbose_name="이미지 높이",
#                               blank=True, null=True, max_length=10)
#     # title = models.CharField(verbose_name="제목",
#     #                          blank=True, null=True, max_length=50)
#     images = models.ImageField(verbose_name="이미지", upload_to="user/profile",
#                                blank=True, null=True)
#     # imagesPath = models.CharField(verbose_name="이미지 경로",
#     #                               blank=True, null=True, max_length=50)

#     def __str__(self):
#         return f"{self.id}-{self.width}-{self.height}"


#     class Meta:
#         verbose_name = "유저 프로필 이미지"
#         verbose_name_plural = "유저 프로필 이미지"


class User(AbstractUser, UserTimeStampedModel):

    def upload_to_func(self, filename):
        prefix = "user/profile"
        file_name = self.name + "_" + str(self.id)
        extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
        return "/".join([prefix, file_name + extension,])

    username = models.CharField(
        verbose_name="아이디", max_length=100, unique=True, blank=True)
    name = models.CharField(
        verbose_name="이름", max_length=50, null=True, blank=True)
    gender = models.CharField(verbose_name="성별", max_length=2, null=True, blank=True)
    profile = models.ImageField(
        verbose_name="프로필 이미지", upload_to=upload_to_func, default="user/profile/basicProfile.jpg")
    userType = models.IntegerField(
        verbose_name="사용자 유형(0-미사용계정, 1-근로자, 2-고용기업, 3-관리자", null=True, blank=True)
    comID = models.ForeignKey("datasets.CompanyList", on_delete=models.SET_NULL,
                                verbose_name="소속 회사", null=True, blank=True)
    team = models.ForeignKey("datasets.TeamList", on_delete=models.SET_NULL,
                                verbose_name="소속 복지관", null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.name}/{self.username}"

    class Meta:
        verbose_name = "이용자"
        verbose_name_plural = "이용자"


class Employee(User):
    age = models.CharField(verbose_name="나이", max_length=50, null=True, blank=True)
    allowedIP = models.ManyToManyField(
        "attendances.IPRegister", verbose_name="허용 아이피", related_name="allowedIP", blank=True)
    attType = models.ForeignKey(
        "attendances.AttendanceType", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="근무유형")
    birthDate = models.CharField(
        verbose_name="생년월일", max_length=100, null=True, blank=True)
    phone = models.CharField(
        verbose_name="연락처", max_length=50, null=True, blank=True)
    userZip = models.CharField(
        verbose_name="우편번호", max_length=50, null=True, blank=True)
    userAddr1 = models.CharField(
        verbose_name="기본주소", max_length=50, null=True, blank=True)
    userAddr2 = models.CharField(
        verbose_name="상세주소", max_length=100, null=True, blank=True)
    sportType = models.ForeignKey(
        "datasets.SportType", on_delete=models.SET_NULL, verbose_name="운동종목", null=True, blank=True)
    teamID = models.ForeignKey(
        "datasets.TeamList", on_delete=models.SET_NULL, verbose_name="훈련기관", null=True, blank=True)
    career = models.IntegerField(verbose_name="선수경력", null=True, blank=True)
    awards = models.TextField(
        verbose_name="수상경력", null=True, blank=True)
    disabilityType = models.ForeignKey("datasets.DisabilityType", on_delete=models.SET_NULL,
                                        verbose_name="장애유형", related_name="disability_type", null=True, blank=True)
    disabilityGrade = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="중증/경증",
                                        limit_choices_to={"maincategory": 1}, related_name="disability_grade", null=True, blank=True)
    height = models.CharField(
        verbose_name="신장", max_length=50, null=True, blank=True)
    weight = models.CharField(
        verbose_name="체중", max_length=50, null=True, blank=True)
    bloodType = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="혈액형", limit_choices_to={"maincategory": 2}, null=True, blank=True)
    wheelchair = models.BooleanField(
        verbose_name="휠체어", default=False, blank=True)
    eyesightL = models.CharField(
        verbose_name="시력(좌)", max_length=50, null=True, blank=True)
    eyesightR = models.CharField(
        verbose_name="시력(우)", max_length=50, null=True, blank=True)
    maritalStatus = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="결혼여부", limit_choices_to={"maincategory": 3}, related_name="marital_status", null=True, blank=True)
    militaryService = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="병역여부", limit_choices_to={
                                        "maincategory": 4}, related_name="military_service", null=True, blank=True)
    education = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="최종학력", limit_choices_to={"maincategory": 5}, related_name="education", null=True, blank=True)
    school = models.CharField(
        verbose_name="학교명", max_length=100, null=True, blank=True)
    department = models.CharField(
        verbose_name="학과명", max_length=50, null=True, blank=True)
    guardianName = models.CharField(
        verbose_name="보호자 이름", max_length=50, null=True, blank=True)
    relation = models.CharField(
        verbose_name="선수와의 관계", max_length=50, null=True, blank=True)
    guardianNum = models.CharField(
        verbose_name="보호자 전화번호", max_length=100, null=True, blank=True)
    guardianEmail = models.EmailField(
        verbose_name="보호자 이메일", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.name}/{self.username}"

    class Meta:
        verbose_name = "근로자"
        verbose_name_plural = "근로자"


@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_save(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    for field in instance._meta.fields:
        field_type = field.get_internal_type()
        if field_type == 'FileField' or field_type == 'ImageField':
            origin_file = getattr(old_obj, field.name)
            new_file = getattr(instance, field.name)
            if origin_file != new_file and os.path.isfile(origin_file.path):
                if origin_file != 'user/profile/basicProfile.jpg':
                    os.remove(origin_file.path)

@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    for field in instance._meta.fields:
        field_type = field.get_internal_type()
        if field_type == 'FileField' or field_type == 'ImageField':
            origin_file = getattr(instance, field.name)
            if origin_file and os.path.isfile(origin_file.path):
                if origin_file != 'user/profile/basicProfile.jpg':
                    os.remove(origin_file.path)