from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser

import os

class User(AbstractUser):
    username = models.CharField(verbose_name="아이디", max_length=50, unique=True, blank=True)
    userType = models.IntegerField(verbose_name="유저타입(0:관리자, 1:기부자", null=True, blank=True)
    storeMaster = models.CharField(verbose_name="대표자명", max_length=50, unique=True, blank=True)
    storeName = models.CharField(verbose_name="가게이름", max_length=50, unique=True, blank=True)
    address = models.CharField(verbose_name="주소", max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name="연락처", max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.storeMaster}/{self.username}"

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저"