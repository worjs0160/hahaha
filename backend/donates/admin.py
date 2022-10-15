from django.contrib import admin
from .models import *

@admin.register(DonateInfo)
class CustomDonateInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "donator",
                    "foodName",
                    "startPickUp",
                    "endPickUp",
                    "comment",
                    "endTime",
                    "foodImage",
                    "commentImage",
                    # "createdTime",
                    # "modifiedTime",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "donator",
        "foodName",
        "startPickUp",
        "endPickUp",
        "comment",
        "endTime",
        "createdTime",
        "modifiedTime",
    )

@admin.register(donateImage)
class CustomDonateImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": (
                    "createUser",
                    "width",
                    "height",
                    "images",
                    "todayOrder",
                )
            }
        )
    ]
    list_display = (
        "createUser",
        "images",
        "createdTime",
        "createUser",
    )

@admin.register(activityImage)
class CustomActivityImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": (
                    "createUser",
                    "width",
                    "height",
                    "images",
                    "todayOrder",
                )
            }
        )
    ]
    list_display = (
        "createUser",
        "images",
        "createdTime",
        "createUser",
    )