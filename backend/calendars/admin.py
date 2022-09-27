from django.contrib import admin
from .models import *

@admin.register(Calendar)
class CustomCalendarAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "start",
        "end",
        "title",
        "contents",
    ]