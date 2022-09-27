from django.db.models.fields import Field
from django_filters import FilterSet, CharFilter, DateTimeFilter, DateFilter

from .models import *


class UserFilter(FilterSet):

    class Meta:
        model = User
        fields = {
            "comID": ['exact'],
        }

    def __init__(self, *args, **kwargs):
        super(UserFilter, self).__init__(*args, **kwargs)
