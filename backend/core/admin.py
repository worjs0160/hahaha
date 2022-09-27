from django.contrib import admin
from .models import *


@admin.register(TimeStampedModel)
class CustomTimeStampedModelAdmin(admin.ModelAdmin):
    list_display = (
        "createdTime",
        "modifiedTime",
        "createUser",
        "modifyUser",
    )


@admin.register(UserTimeStampedModel)
class CustomUserTimeStampedModelAdmin(admin.ModelAdmin):
    list_display = (
        "createdTime",
        "modifiedTime",
        "createUser",
        "modifyUser",
    )