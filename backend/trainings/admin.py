from django.contrib import admin
from .models import *


@admin.register(Training)
class CustomTrainingAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "workDate",
                    "title",
                    "contents",
                    "state",
                    "images",
                    "reason",
                    "rejectedTime",
                    "rejectedReason",
                )
            }
        )
    ]
    list_display = (
        "user",
        "workDate",
        "title",
        "contents",
    )
