# from django.contrib import admin
# from .models import Training


# @admin.register(Training)
# class CustomTrainingAdmin(admin.ModelAdmin):
#     readonly_fields = ("created", "updated")

#     fieldsets = [
#         (
#             "훈련관리",
#             {
#                 "fields": [
#                     "user",
#                     "coach",
#                     "trainingDate",
#                     "contents",
#                     "created",
#                     "updated",
#                 ]
#             },
#         )
#     ]

#     list_display = ("user", "coach", "trainingDate", "contents", "created", "updated")