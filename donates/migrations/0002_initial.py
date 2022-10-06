# Generated by Django 4.1.2 on 2022-10-07 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("donates", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="donateinfo",
            name="donater",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="donatesInfo",
                to=settings.AUTH_USER_MODEL,
                verbose_name="기부자",
            ),
        ),
    ]
