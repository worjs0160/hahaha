# from django.db import models


# class Attendance(models.Model):
#     user = models.ForeignKey(
#         "users.User",
#         related_name="attendances",
#         on_delete=models.CASCADE,
#         verbose_name="선수",
#     )
#     startWorkTime = models.CharField(
#         max_length=30,
#         blank=True,
#         null=True,
#         verbose_name="출근시간",
#     )
#     finishWorkTime = models.CharField(
#         max_length=30, null=True, blank=True, verbose_name="퇴근시간"
#     )
#     workPlace = models.TextField(null=True, blank=True, verbose_name="출근장소")
    
#     memo = models.TextField(null=True, blank=True, verbose_name="메모")

#     class Meta:
#         verbose_name = "근태정보"
#         verbose_name_plural = "근태정보"

#     def __str__(self):
#         return f"{self.user.name} ID:{self.id}"

#     # def save(self, *args, **kwargs):
#     #     super().save(*args, **kwargs)