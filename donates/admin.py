from django.contrib import admin

from django.contrib import admin
from .models import *

@admin.register(DonateInfo)
class CustomDonateInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "donater",
                    "foodName",
                    "startPickUp",
                    "endPickUp",
                    "comment",
                    "endTime",
                    "foodImage",
                    # "createdTime",
                    # "modifiedTime",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "donater",
        "foodName",
        "startPickUp",
        "endPickUp",
        "comment",
        "endTime",
        "foodImage",
        "createdTime",
        "modifiedTime",
    )
