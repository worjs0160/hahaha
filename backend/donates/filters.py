from django_filters import FilterSet, CharFilter, DateTimeFilter, DateFilter

from .models import *


class FoodImageFilter(FilterSet):
    createdTime = CharFilter(field_name="createdTime", lookup_expr="icontains")

    class Meta:
        model = donateImage
        fields = {
            "createUser": ['exact'],
        }

class ActivityImageFilter(FilterSet):
    createdTime = CharFilter(field_name="createdTime", lookup_expr="icontains")

    class Meta:
        model = activityImage
        fields = {
            "createUser": ['exact'],
        }