from datetime import datetime
from rest_framework import serializers

from .models import *
from users.models import *
from datasets.models import *
from users.serializers import *


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = "__all__"


class MonthlyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyReport
        fields = "__all__"


class CompetitionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionReport
        fields = "__all__"


class VacationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationReport
        fields = "__all__"
