from rest_framework import serializers


from .models import *
from users.models import *
from datasets.models import *
from users.serializers import *

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"
