from django.dispatch import receiver
from django.db import models
from core.models import *

from uuid import uuid4

import os


class Player(UserTimeStampedModel):
    # 선정 기업
    comID = models.ForeignKey("datasets.CompanyList", on_delete=models.SET_NULL,
                                verbose_name="소속 회사", null=True, blank=True)

    def upload_to_func(self, filename):
        prefix = "consultings/profile"
        file_name = self.name + "_" + str(self.id)
        extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
        return "/".join([prefix, file_name + extension,])

    # 기본사항
    name = models.CharField(verbose_name="이름", max_length=50, null=True, blank=True)
    profile = models.ImageField(verbose_name="프로필 이미지", upload_to=upload_to_func, default="consultings/profile/basicProfile.jpg")
    age = models.CharField(verbose_name="나이", max_length=50, null=True, blank=True)
    gender = models.CharField(verbose_name="성별", max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name="연락처", max_length=50, null=True, blank=True)
    birthDate = models.CharField(verbose_name="생년월일", max_length=100, null=True, blank=True)
    userZip = models.CharField(verbose_name="우편번호", max_length=50, null=True, blank=True)
    userAddr1 = models.CharField(verbose_name="기본주소", max_length=50, null=True, blank=True)
    userAddr2 = models.CharField(verbose_name="상세주소", max_length=100, null=True, blank=True)

    # 경력사항
    sportType = models.ForeignKey("datasets.SportType", on_delete=models.SET_NULL, verbose_name="운동종목", null=True, blank=True)
    career = models.IntegerField(verbose_name="선수경력", null=True, blank=True)
    awards = models.TextField(verbose_name="수상경력", max_length=100, null=True, blank=True)
    team = models.ForeignKey("datasets.TeamList", on_delete=models.SET_NULL, verbose_name="소속 복지관", null=True, blank=True)
    
    # 개인사항
    disabilityType = models.ForeignKey("datasets.DisabilityType", on_delete=models.SET_NULL, verbose_name="장애유형", related_name="players_disabilityType", null=True, blank=True)
    disabilityGrade = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="중증/경증", limit_choices_to={"maincategory": 1}, related_name="players_disabilityGrade", null=True, blank=True)
    height = models.CharField(verbose_name="신장", max_length=50, null=True, blank=True)
    weight = models.CharField(verbose_name="체중", max_length=50, null=True, blank=True)
    bloodType = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="혈액형", limit_choices_to={"maincategory": 2}, null=True, blank=True)
    wheelchair = models.BooleanField(verbose_name="휠체어", default=False, blank=True)
    eyesightL = models.CharField(verbose_name="시력(좌)", max_length=50, null=True, blank=True)
    eyesightR = models.CharField(verbose_name="시력(우)", max_length=50, null=True, blank=True)
    maritalStatus = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="결혼여부", limit_choices_to={"maincategory": 3}, related_name="players_maritalStatus", null=True, blank=True)
    militaryService = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="병역여부", limit_choices_to={"maincategory": 4}, related_name="players_militaryService", null=True, blank=True)
    education = models.ForeignKey("datasets.SubCategory", on_delete=models.SET_NULL, verbose_name="최종학력", limit_choices_to={"maincategory": 5}, related_name="players_education", null=True, blank=True)
    school = models.CharField(verbose_name="학교명", max_length=100, null=True, blank=True)
    department = models.CharField(verbose_name="학과명", max_length=50, null=True, blank=True)
    guardianName = models.CharField(verbose_name="보호자 이름", max_length=50, null=True, blank=True)
    relation = models.CharField(verbose_name="선수와의 관계", max_length=50, null=True, blank=True)
    guardianNum = models.CharField(verbose_name="보호자 전화번호", max_length=100, null=True, blank=True)
    guardianEmail = models.EmailField(verbose_name="보호자 이메일", max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.id}-{self.name}"

    class Meta:
        verbose_name = "컨설팅 유저"
        verbose_name_plural = "컨설팅 유저"

@receiver(models.signals.pre_save, sender=Player)
def auto_delete_file_on_save(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    for field in instance._meta.fields:
        field_type = field.get_internal_type()
        if field_type == 'FileField' or field_type == 'ImageField': # Player 모델에서 File, Image Field 찾음
            origin_file = getattr(old_obj, field.name) # 해당 Player가 가진 파일의 이름
            new_file = getattr(instance, field.name) # 새롭게 등록될 파일의 이름
            if origin_file != new_file and os.path.isfile(origin_file.path): # 원래의 파일과 새로운 파일의 이름이 다르면 기존의 파일 삭제
                if origin_file != 'consultings/profile/basicProfile.jpg':
                    os.remove(origin_file.path)

@receiver(models.signals.post_delete, sender=Player)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    for field in instance._meta.fields:
        field_type = field.get_internal_type()
        if field_type == 'FileField' or field_type == 'ImageField':
            origin_file = getattr(instance, field.name)
            if origin_file and os.path.isfile(origin_file.path):
                if origin_file != 'consultings/profile/basicProfile.jpg':
                    os.remove(origin_file.path)