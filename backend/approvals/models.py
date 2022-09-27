from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel
from users.models import *
from trainings.models import *

class Approval(TimeStampedModel):
    title = models.CharField(verbose_name="제목", max_length=100, null=True, blank=True) 
    user = models.ForeignKey("users.Employee", related_name="approval", on_delete=models.CASCADE, verbose_name="기안자")
    approver =models.ForeignKey("users.User", related_name="approver", on_delete=models.CASCADE, verbose_name="결재자")
    prepareTime = models.DateTimeField(verbose_name="기안일", null=True, blank=True)
    approvalTime = models.DateTimeField(verbose_name="결재일", null=True, blank=True)
    approvalStatus = models.BooleanField(verbose_name="승인여부", default=False, blank=True)

    def __str__(self):
        return f"{self.id}/{self.user.name}/{self.approvalStatus}"

    class Meta:
        verbose_name = "전자결재"
        verbose_name_plural = "전자결재"


class MonthlyReport(Approval):
    contents = models.ManyToManyField("trainings.Training", verbose_name="훈련일지", blank=True)

    def __str__(self):
        return f"{self.id}/{self.user.name}/{self.title}"

    class Meta:
        verbose_name = "월간업무보고"
        verbose_name_plural = "월간업무보고"


class CompetitionReport(Approval):
    startTime = models.DateTimeField(verbose_name="시작일자", null=True, blank=True)
    endtTime = models.DateTimeField(verbose_name="종료일자", null=True, blank=True) 
    partner = models.CharField(verbose_name="동행자", max_length=100, null=True, blank=True) 
    contents = models.TextField(verbose_name="대회내용", max_length=100, null=True, blank=True)
    movingPlan = models.TextField(verbose_name="이동방안", max_length=100, null=True, blank=True)
    preparePlan = models.TextField(verbose_name="준비사항", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.user.name}/{self.title}"

    class Meta:
        verbose_name = "대회참가계획서"
        verbose_name_plural = "대회참가계획서"


class VacationReport(Approval):

    VACATION_HALF = "half"
    VACATION_DAY = "day"
    VACATION_MORNING = "morning"
    VACATION_AFTERNOON = "afternoon"
    VACATION_SICK = "sick"

    VACATION_CHOICES = (
        (VACATION_HALF, _("half")),
        (VACATION_DAY, _("day")),
        (VACATION_MORNING, _("morning")),
        (VACATION_AFTERNOON, _("afternoon")),
        (VACATION_SICK, _("sick")),
    )

    vacationType = models.CharField(_("휴가종류"), choices=VACATION_CHOICES, max_length=15, blank=True)
    startTime = models.DateTimeField(verbose_name="휴가시작시간", null=True, blank=True)
    endtTime = models.DateTimeField(verbose_name="휴가종료시간", null=True, blank=True) 
    halfTime = models.BooleanField(verbose_name="0:오전 1:오후", default=False, blank=True)
    memo = models.TextField(verbose_name="휴가사유", max_length=100, null=True, blank=True)



    def __str__(self):
        return f"{self.id}/{self.user.name}/{self.title}/{self.vacationType}"

    class Meta:
        verbose_name = "휴가신청서"
        verbose_name_plural = "휴가신청서"