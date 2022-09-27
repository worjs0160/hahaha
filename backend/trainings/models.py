from django.db import models
from core.models import TimeStampedModel

class TrainingImage(TimeStampedModel):
    width = models.CharField(verbose_name="이미지 너비",
                             blank=True, null=True, max_length=10)
    height = models.CharField(verbose_name="이미지 높이",
                              blank=True, null=True, max_length=10)
    # title = models.CharField(verbose_name="제목",
    #                          blank=True, null=True, max_length=50)
    images = models.ImageField(verbose_name="이미지", upload_to="trainings/trainingImg",
                               blank=True, null=True)
    # imagesPath = models.CharField(verbose_name="이미지 경로",
    #                               blank=True, null=True, max_length=50)
    

    class Meta:
        verbose_name = "훈련 이미지"
        verbose_name_plural = "훈련 이미지"

class Training(TimeStampedModel):
    user = models.ForeignKey("users.User", related_name="trainings", on_delete=models.CASCADE, verbose_name="근로자", default='1')  # 선수의 아이디
    workDate = models.DateTimeField(verbose_name="작성일", null=True, blank=True)
    contents = models.TextField(verbose_name="내용", null=True, blank=True)
    title = models.CharField(
        verbose_name="제목", max_length=100, null=True, blank=True)
        
    state = models.IntegerField(
        verbose_name="업무일지 상태(0-미승인, 1-승인, 2-반려", default="0", blank=True)
    # attType = models.ForeignKey(
    #     "attendances.AttendanceType", related_name="trainings", on_delete=models.RESTRICT, verbose_name="근태유형")
    
    images = models.ManyToManyField(
        "TrainingImage",
        verbose_name="훈련 이미지",
        blank=True,
    )
    reason = models.TextField(verbose_name="사유", max_length=100, null=True, blank=True)
    rejectedReason = models.TextField(verbose_name="반려사유", max_length=100, null=True, blank=True)
    rejectedTime = models.DateTimeField(verbose_name="반려일시", null=True, blank=True)

    def __str__(self):
        return f"{self.user}/{self.workDate}"

    class Meta:
        verbose_name = "훈련일지"
        verbose_name_plural = "훈련일지"
