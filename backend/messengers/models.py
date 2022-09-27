from django.db import models

class Messenger(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='messengers', verbose_name="사용자", default='1')    
    roomNum = models.CharField(max_length=10, blank=True, verbose_name="방 번호")
    message = models.CharField(max_length=1200, blank=True, verbose_name="내용")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="보낸 시간")
    isRead = models.BooleanField(default=False, verbose_name="확인 여부")

    def __str__(self):
        return f"{self.user.name}: {self.message}"
    class Meta:
        verbose_name = "메신저"
        verbose_name_plural = "메신저"
        ordering = ('timestamp',)
    