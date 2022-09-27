from django.contrib import admin
from .models import *


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "username",
                    "password",
                    "name",
                    "profile",
                    "email",
                    "userType",
                    "comID",
                    "team",
                    "createUser",
                    "modifyUser",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "username",
        "name",
        "is_active",
        "is_staff",
        "is_superuser",
        "createdTime",
        "modifiedTime"
    )


@admin.register(Employee)
class CustomEmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "기본정보",
            {
                "fields": [
                    "username",
                    "name",
                    "profile",
                    "phone",
                    "gender",
                    "email",
                    "attType",
                    "birthDate",
                    "userZip",
                    "userAddr1",
                    "userAddr2",
                    "sportType",
                    "teamID",
                    "career",
                    "awards",
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
                    "createUser",
                    "modifyUser",
                    "allowedIP",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "username",
        "name",
        "teamID",
        "comID",
        "attType",
        "createdTime",
        "modifiedTime",
    )


# @admin.register(Profile)
# class CustomProfileAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (
#             "기본정보",
#             {
#                 "fields": [
#                     "width",
#                     "height",
#                     "images",
#                 ]
#             },
#         ),
#     ]
#     list_display = (
#         "id",
#         "width",
#         "height",
#     )