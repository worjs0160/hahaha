from django.db import models
from core.models import TimeStampedModel


class AttendanceType(TimeStampedModel):
    name = models.CharField(verbose_name="유형이름",
                            max_length=100, null=True, blank=True)
    onTime = models.CharField(
        verbose_name="출근시간", max_length=100, null=True, blank=True)
    offTime = models.CharField(
        verbose_name="퇴근시간", max_length=100, null=True, blank=True)
    monthWorkTime = models.CharField(
        verbose_name="월근무시간", max_length=100, null=True, blank=True)
    workDay = models.ManyToManyField("datasets.SubCategory", verbose_name="근무요일", limit_choices_to={
        "maincategory": 7}, related_name="work_day", blank=True)

    def __str__(self):
        return f"{self.id}/{self.name}/{self.onTime}/{self.offTime}"

    class Meta:
        verbose_name = "근태유형"
        verbose_name_plural = "근태유형"


class Attendance(TimeStampedModel):
    user = models.ForeignKey("users.User", related_name="attendances", on_delete=models.CASCADE, verbose_name="근로자", default='1')
    attType = models.ForeignKey("attendances.AttendanceType", related_name="attendances", on_delete=models.RESTRICT, verbose_name="근태유형")
    onTime = models.DateTimeField(verbose_name="출근시간", null=True, blank=True)
    onType = models.BooleanField(
        verbose_name="출근구분", default=False, blank=True)
    onContent = models.TextField(verbose_name="출근비고", null=True, blank=True)
    offTime = models.DateTimeField(verbose_name="퇴근시간", null=True, blank=True)
    offType = models.BooleanField(
        verbose_name="퇴근구분", default=False, blank=True)
    offContent = models.TextField(verbose_name="퇴근비고", null=True, blank=True)
    place = models.CharField(
        verbose_name="근무지", max_length=100, null=True, blank=True)
    IP = models.CharField(verbose_name="근무지", max_length=100, null=True, blank=True)
    workTime = models.CharField(
        verbose_name="근무시간", max_length=100, null=True, blank=True)
    memo = models.TextField(verbose_name="메모", null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.user}/{self.onTime}/{self.offTime}"

    class Meta:
        verbose_name = "근태정보"
        verbose_name_plural = "근태정보"


class IPRegister(TimeStampedModel):
    company = models.ForeignKey("datasets.CompanyList", related_name="ipRegisters", on_delete=models.CASCADE, verbose_name="고용기업")
    title = models.CharField(verbose_name="제목", max_length=100, null=True, blank=True)
    permissionIP = models.CharField(verbose_name="허용 IP", max_length=100, null=True, blank=True)
    place = models.CharField(verbose_name="근무지", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}/{self.company}/{self.title}/{self.permissionIP}"

    class Meta:
        verbose_name = "근태 허용 IP 관리"
        verbose_name_plural = "근태 허용 IP 관리"