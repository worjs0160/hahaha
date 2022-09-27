from django.contrib import admin
from .models import *

@admin.register(Approval)
class CustomApprovalAdmin(admin.ModelAdmin):
    fieldset = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "approver",
                    "prepareTime",
                    "approvalTime",
                    "approvalStatus",
                )
            }
        )
    ]
    list_display = (
        "id",
        "user",
        "approver",
        "prepareTime",
        "approvalTime",
        "approvalStatus",
    )

@admin.register(MonthlyReport)
class CustomMonthlyReportAdmin(admin.ModelAdmin):
    fieldset = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "approver",
                    "prepareTime",
                    "approvalTime",
                    "approvalStatus",
                    "contents",
                )
            }
        )
    ]
    list_display = (
        "id",
        "user",
        "approver",
        "prepareTime",
        "approvalTime",
        "approvalStatus",
    )

@admin.register(CompetitionReport)
class CustomCompetitionReportAdmin(admin.ModelAdmin):
    fieldset = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "approver",
                    "prepareTime",
                    "approvalTime",
                    "approvalStatus",
                    "contents",
                    "startTime",
                    "endTime",
                    "partner",
                    "movingPlan",
                    "preparePlan",
                )
            }
        )
    ]
    list_display = (
        "id",
        "user",
        "approver",
        "prepareTime",
        "approvalTime",
        "approvalStatus",
    )

@admin.register(VacationReport)
class CustomVacationReportAdmin(admin.ModelAdmin):
    fieldset = [
        (
            "기본정보",
            {
                "fields": (
                    "user",
                    "approver",
                    "prepareTime",
                    "approvalTime",
                    "approvalStatus",
                    "contents",
                    "vacationType",
                    "startTime",
                    "endtTime",
                    "halfTime",
                    "memo",
                )
            }
        )
    ]
    list_display = (
        "id",
        "user",
        "approver",
        "prepareTime",
        "approvalTime",
        "approvalStatus",
    )