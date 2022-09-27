from django.contrib.auth.models import AbstractUser
from django.db import models


class UserTimeStampedModel(models.Model):
    createdTime = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    createUser = models.IntegerField(verbose_name="생성자", null=True, blank=True, default=None)
    modifyUser = models.IntegerField(verbose_name="변경자", null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.id}-{self.createdTime}-{self.modifiedTime}"

    class Meta:
        verbose_name = "유저용 타임스탬프"
        verbose_name_plural = "유저용 타임스탬프"


class TimeStampedModel(models.Model):
    createdTime = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
    modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
    createUser = models.IntegerField(verbose_name="생성자", null=True, blank=True, default=None)
    modifyUser = models.IntegerField(verbose_name="변경자", null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.id}-{self.createdTime}-{self.modifiedTime}"

    class Meta:
        verbose_name = "타임스탬프"
        verbose_name_plural = "타임스탬프"
    

# class RecordTimeStampedModel(models.Model):
#     createdTime = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)
#     modifiedTime = models.DateTimeField(verbose_name="수정일시", auto_now=True)
#     createUser = models.IntegerField(verbose_name="생성자", null=True, blank=True, default=None)
#     modifyUser = models.IntegerField(verbose_name="변경자", null=True, blank=True, default=None)

#     class Meta:
#         verbose_name = "타임스탬프"
#         verbose_name_plural = "타임스탬프"


# class log(models.Model):
#     connetDate = models.DateTimeField(verbose_name="접속일시")
#     ip = models.CharField(verbose_name="생성일시")