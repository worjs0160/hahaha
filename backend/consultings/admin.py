from django.contrib import admin
from .models import *

@admin.register(Player)
class CustomPlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "선정기업",
            {
                "fields": [
                    "comID",
                ]
            },
        ),
        (
            "기본사항",
            {
                "fields": [
                    "name",
                    "profile",
                    "gender",
                    "phone",
                    "birthDate",
                    "userZip",
                    "userAddr1",
                    "userAddr2",
                ]
            },
        ),
        (
            "경력사항",
            {
                "fields": [
                    "sportType",
                    "career",
                    "awards",
                    "team",
                ]
            },
        ),
        (
            "개인사항",
            {
                "fields": [
                    "disabilityType",
                    "disabilityGrade",
                    "height",
                    "weight",
                    "bloodType",
                    "wheelchair",
                    "eyesightL",
                    "eyesightR",
                    "maritalStatus",
                    "militaryService",
                    "education",
                    "school",
                    "department",
                    "guardianName",
                    "relation",
                    "guardianNum",
                    "guardianEmail",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "name",
        "createdTime",
        "modifiedTime"
    )