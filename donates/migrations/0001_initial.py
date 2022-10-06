# Generated by Django 4.1.2 on 2022-10-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DonateInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "foodName",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="기부 음식명"
                    ),
                ),
                (
                    "createdTime",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록일시"),
                ),
                (
                    "modifiedTime",
                    models.DateTimeField(auto_now=True, verbose_name="수정일시"),
                ),
                (
                    "startPickUp",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="픽업 가능시간(시작)"
                    ),
                ),
                (
                    "endPickUp",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="픽업 가능시간(종료)"
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="코멘트"
                    ),
                ),
                (
                    "endTime",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="처리일자"
                    ),
                ),
                (
                    "foodImage",
                    models.ImageField(
                        default=None, upload_to="donates", verbose_name="음식사진"
                    ),
                ),
            ],
            options={"verbose_name": "기부내용", "verbose_name_plural": "기부내용",},
        ),
    ]
