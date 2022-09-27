from django.db.models.fields import Field
from django_filters import DateFromToRangeFilter, IsoDateTimeFromToRangeFilter, FilterSet, CharFilter, DateTimeFilter, DateFilter, DateTimeFromToRangeFilter, DateRangeFilter

from .models import *
from users.models import *


class AttendanceFilter(FilterSet):
    comID = CharFilter(field_name="user", lookup_expr="comID")
    teamID = CharFilter(field_name="user", lookup_expr="teamID")

    class Meta:
        model = Attendance
        fields = {
            "user_id": ['exact'],
            "onTime": ['range'],
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceFilter, self).__init__(*args, **kwargs)


class UserAttFilter(FilterSet):
    # onTime = DateFromToRangeFilter(field_name="attendances__onTime", lookup_expr="onTime")
    # onTime2 = CharFilter(field_name="attendances", lookup_expr="onTime")
    # onTime = DateFilter(field_name="attendances", lookup_expr="onTime")
    # onTime = IsoDateTimeFromToRangeFilter(field_name="attendances", lookup_expr="onTime")

    class Meta:
        model = User
        fields = {
            "id": ['exact'],
            "comID": ['exact'],
            "userType": ['exact'],
        }

    def __init__(self, *args, **kwargs):
        super(UserAttFilter, self).__init__(*args, **kwargs)
