# from django.db import models


# class Calendar(models.Model):
#     user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="calendar", verbose_name="선수")
#     title = models.CharField(verbose_name="제목", max_length=20, blank=True, null=True)
#     date = models.CharField(verbose_name="날짜", max_length=20, blank=True, null=True)
#     content = models.TextField(verbose_name="내용", blank=True, null=True)
#     sportType = models.ForeignKey("datasets.SportType", on_delete=models.CASCADE, related_name="calendar", verbose_name="종목")

#     class Meta:
#         verbose_name = "일정"
#         verbose_name_plural = "일정"