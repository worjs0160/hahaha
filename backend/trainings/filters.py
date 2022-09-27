from django_filters import FilterSet, CharFilter, DateTimeFilter, DateFilter

from .models import *

class TrainingFilter(FilterSet):
    comID = CharFilter(field_name="user", lookup_expr="comID")
    teamID = CharFilter(field_name="user", lookup_expr="teamID")

    class Meta:
        model = Training
        fields = {
            "user_id": ['exact'],
            "workDate": ['range'],
        }
