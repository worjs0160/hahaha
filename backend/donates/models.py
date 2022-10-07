from email.policy import default
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class DonateInfo(models.Model):
    donater = models.ForeignKey("users.User", related_name="donatesInfo", on_delete=models.CASCADE ,verbose_name="기부자")
    foodName = models.CharField(verbose_name="기부 음식명", max_length=50, null=True, blank=True)
    createdTime = models.DateTimeField(verbose_name="등록일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    startPickUp = models.CharField(verbose_name="픽업 가능시간(시작)", max_length=50, null=True, blank=True)
    endPickUp = models.CharField(verbose_name="픽업 가능시간(종료)", max_length=50, null=True, blank=True)
    comment = models.CharField(verbose_name="코멘트", max_length=50, null=True, blank=True)
    endTime = models.CharField(verbose_name="처리일자", max_length=50, null=True, blank=True)
    foodImage = models.ImageField(verbose_name="음식사진", upload_to="donates", default=None, null=True, blank=True)
    state = models.CharField(verbose_name="기부상태(0:처리 필요, 1:완료)", max_length=50, null=True, blank=True, default="0")

    def __str__(self):
        return f"{self.id}/{self.donater.storeMaster}"

    class Meta:
        verbose_name = "기부내용"
        verbose_name_plural = "기부내용"