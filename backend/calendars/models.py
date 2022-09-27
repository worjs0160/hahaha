from django.db import models


class Calendar(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="calendar", verbose_name="선수", default='1')
    title = models.CharField(verbose_name="제목", max_length=20, blank=True, null=True)
    start = models.DateTimeField(verbose_name="시작날짜", blank=True, null=True)
    end = models.DateTimeField(verbose_name="종료날짜", blank=True, null=True)
    contents = models.TextField(verbose_name="내용", blank=True, null=True)
    startEditable = models.BooleanField(verbose_name="드래그 수정 여부", default=True, blank=True)
    
    def __str__(self):
        return f"{self.user}/{self.start}/{self.end}"

    class Meta:
        verbose_name = "일정"
        verbose_name_plural = "일정"