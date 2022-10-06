# Generated by Django 4.1.2 on 2022-10-07 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donates", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="donateinfo",
            name="state",
            field=models.CharField(
                blank=True,
                default="0",
                max_length=50,
                null=True,
                verbose_name="기부상태(0:처리 필요, 1:완료)",
            ),
        ),
        migrations.AlterField(
            model_name="donateinfo",
            name="foodImage",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="donates",
                verbose_name="음식사진",
            ),
        ),
    ]
