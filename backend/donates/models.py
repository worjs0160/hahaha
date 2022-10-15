from email.policy import default
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class donateImage(models.Model):
    createdTime = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    createUser = models.IntegerField(verbose_name="생성자", null=True, blank=True, default=None)
    modifyUser = models.IntegerField(verbose_name="변경자", null=True, blank=True, default=None)
    width = models.CharField(verbose_name="이미지 너비", blank=True, null=True, max_length=10)
    height = models.CharField(verbose_name="이미지 높이", blank=True, null=True, max_length=10)
    images = models.ImageField(verbose_name="이미지", upload_to="donates/foodImages", blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.createdTime}-{self.modifiedTime}"
    
    class Meta:
        verbose_name = "음식 이미지"
        verbose_name_plural = "음식 이미지"


class activityImage(models.Model):
    createdTime = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    createUser = models.IntegerField(verbose_name="생성자", null=True, blank=True, default=None)
    modifyUser = models.IntegerField(verbose_name="변경자", null=True, blank=True, default=None)
    width = models.CharField(verbose_name="이미지 너비", blank=True, null=True, max_length=10)
    height = models.CharField(verbose_name="이미지 높이", blank=True, null=True, max_length=10)
    images = models.ImageField(verbose_name="이미지", upload_to="donates/activityImages", blank=True, null=True)

    def __str__(self):
        return f"{self.id}-{self.createdTime}-{self.modifiedTime}"
    
    class Meta:
        verbose_name = "활동 이미지"
        verbose_name_plural = "활동 이미지"


class DonateInfo(models.Model):
    donator = models.ForeignKey("users.User", related_name="donatesInfo", on_delete=models.CASCADE ,verbose_name="기부자")
    foodName = models.CharField(verbose_name="기부 음식명", max_length=50, null=True, blank=True)
    createdTime = models.DateTimeField(verbose_name="등록일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    startPickUp = models.CharField(verbose_name="픽업 가능시간(시작)", max_length=50, null=True, blank=True)
    endPickUp = models.CharField(verbose_name="픽업 가능시간(종료)", max_length=50, null=True, blank=True)
    comment = models.CharField(verbose_name="코멘트", max_length=50, null=True, blank=True)
    endTime = models.CharField(verbose_name="처리일자", max_length=50, null=True, blank=True)
    foodImage = models.ManyToManyField(
        "donateImage",
        verbose_name="음식 이미지",
        blank=True,
    )
    commentImage = models.ManyToManyField(
        "activityImage",
        verbose_name="활동 이미지",
        blank=True,
    )
    state = models.CharField(verbose_name="기부상태(0:처리 필요, 1:완료)", max_length=50, null=True, blank=True, default="0")

    def __str__(self):
        return f"{self.id}/{self.donator.storeMaster}"

    class Meta:
        verbose_name = "기부내용"
        verbose_name_plural = "기부내용"
        
