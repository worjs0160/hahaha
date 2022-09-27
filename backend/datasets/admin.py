from django.contrib import admin
from .models import *


# 공통코드 인라인 데이터
class SubCatInline(admin.StackedInline):
    model = SubCategory


# 공통코드 데이터 어드민
@admin.register(MainCategory)
class CommonDataAdmin(admin.ModelAdmin):
    inlines = (SubCatInline,) # inline을 사용하여 SubCatInline 데이터를 삽입 
 

# 장애유형 어드민
@admin.register(DisabilityType)
class CustomDisabilityTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
    )


# 운동종목 어드민
@admin.register(SportType)
class CustomSportTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
    )


# 기업목록 어드민
@admin.register(CompanyList)
class CustomCompanyListeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "comName",
        "ceoName",
        "businessNum",
        "comZip",
        "comAddr1",
        "comAddr2",
        "logoPath",
        "latitude",
        "longitude",
    )


# 복지관(훈련기관)목록 어드민
@admin.register(TeamList)
class CustomTeamListeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "teamName",
        "logoPath",
        "allowedIP",
        "longitude",
        "latitude",
    )
