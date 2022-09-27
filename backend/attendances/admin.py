from django.contrib import admin
from .models import *


@admin.register(AttendanceType)
class CustomAttendanceTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": (
                    "name",
                    "onTime",
                    "offTime",
                    "monthWorkTime",
                    "workDay",
                )
            }
        )
    ]
    list_display = (
        "name",
        "onTime",
        "offTime",
        "monthWorkTime",
    )


@admin.register(Attendance)
class CustomAttendanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "attType",
                    "onTime",
                    "onType",
                    "onContent",
                    "offTime",
                    "offType",
                    "offContent",
                    "place",
                    "workTime",
                    "memo",
                )
            }
        )
    ]
    list_display = (
        "user",
        "attType",
        "onTime",
        "offTime",
        "workTime",
    )


@admin.register(IPRegister)
class CustomIPRegisterAdmin(admin.ModelAdmin):
    fieldset = [
        (
            "기본정보",
            {
                "fields": (
                    "company",
                    "title",
                    "permissionIP",
                    "place",
                )
            }
        )
    ]
    list_display = (
        "company",
        "title",
        "permissionIP",
        "place"
    )