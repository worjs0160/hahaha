# from django.db import models


# class Training(models.Model):

#     created = models.DateTimeField(verbose_name="생성일시", auto_now_add=True)  # 데이터 생성 날짜
#     updated = models.DateTimeField(
#         verbose_name="수정일시",
#         auto_now=True,
#     )  # 데이터 수정 날짜
#     trainingDate = models.CharField(
#         verbose_name="훈련일시", max_length=10, null=False
#     )  # 훈련날짜
#     contents = models.TextField(verbose_name="훈련내용", blank=True)  # 훈련내용
#     coach = models.ForeignKey(
#         "users.User",
#         verbose_name="코치",
#         related_name="usersTraining",
#         on_delete=models.CASCADE,
#     )  # 코치(작성자)의 아이디
#     user = models.ForeignKey(
#         "users.User",
#         verbose_name="선수",
#         related_name="myTraining",
#         on_delete=models.CASCADE,
#     )  # 선수의 아이디

#     def __str__(self):
#         return f"{self.contents}-{self.trainingDate}"

#     class Meta:
#         verbose_name = "훈련"
#         verbose_name_plural = "훈련"
