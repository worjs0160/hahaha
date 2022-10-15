from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class User(AbstractUser):
    username = models.CharField(verbose_name="아이디", max_length=50, unique=True, blank=True)
    userType = models.IntegerField(verbose_name="유저타입(0:관리자, 1:기부자", null=True, blank=True)
    storeMaster = models.CharField(verbose_name="대표자명", max_length=50, null=True, blank=True)
    storeName = models.CharField(verbose_name="가게이름", max_length=50, unique=True, blank=True)
    userZip = models.CharField(verbose_name="우편번호", max_length=50, null=True, blank=True)
    userAddr1 = models.CharField(verbose_name="기본주소", max_length=50, null=True, blank=True)
    userAddr2 = models.CharField(verbose_name="상세주소", max_length=100, null=True, blank=True)
    phone = models.CharField(verbose_name="연락처", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.storeMaster}/{self.username}"

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저"