# from django.contrib import admin
# from .models import AuthSms, User


# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):

#     fieldsets = [
#         (
#             "기본정보",
#             {
#                 "fields": [
#                     "username",
#                     "password",
#                     "name",
#                     "birthDate",
#                     "gender",
#                     "email",
#                     "phoneNum",
#                     "userZip",
#                     "userAddr1",
#                     "userAddr2",
#                     "profileImgSrc",
#                     "userType",
#                     "coach",
#                 ]
#             },
#         ),
#         (
#             "경력사항",
#             {
#                 "fields": [
#                     "sportType",
#                     "team",
#                     "company",
#                     "career",
#                 ]
#             },
#         ),
#         (
#             "개인사항",
#             {
#                 "fields": [
#                     "disabilityType",
#                     "disabilityGrade",
#                     "height",
#                     "weight",
#                     "bloodType",
#                     "wheelchair",
#                     "eyesightL",
#                     "eyesightR",
#                     "maritalStatus",
#                     "militaryService",
#                     "education",
#                     "school",
#                     "department",
#                     "monthWorkTime",
#                     "workDay",
#                     "trainingStartTime",
#                     "trainingFinishTime",
#                     "companyPermission",

#                 ]
#             },
#         ),
#         (
#             "보호자 정보",
#             {
#                 "fields": [
#                     "guardianName",
#                     "relation",
#                     "guardianNum",
#                     "guardianEmail",
#                     "subGuardianName",
#                     "subRelation",
#                     "subGuardianNum",
#                     "subGuardianEmail",
#                 ]
#             },
#         ),
#          (
#             "기관 정보",
#             {
#                 "fields": [
#                     "divisionName",
#                     "divisionNum",
#                 ]
#             },
#         ),
#         (
#             "권한",
#             {
#                 "fields": [
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                 ]
#             },
#         ),
#         (
#             "기타",
#             {
#                 "fields": [
#                     "last_login",
#                     "date_joined",
#                 ]
#             },
#         ),
#     ]

#     list_display = (
#         "id",
#         "userType",
#         "username",
#         "name",
#         "team",
#         "company",
#         "coach",
#         "email",
#         "is_active",
#         "disabilityType",
#         "is_staff",
#         "is_superuser",
#     )

# @admin.register(AuthSms)
# class CustomAuthSmsAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (
#             "인증",
#             {
#                 "fields": [
#                     "phoneNum",
#                     "authNum",
#                 ]
#             },
#         )
#     ]

#     list_display = ("phoneNum", "authNum",)