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
                    "userType",
                    "storeMaster",
                    "storeName",
                    "address",
                    "phone",
                ]
            },
        ),
    ]
    list_display = (
        "id",
        "username",
        "userType",
        "storeMaster",
        "storeName",
        "address",
        "phone"
    )
