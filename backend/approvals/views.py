from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .serializers import *
# from .filters import *

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    filter_backends = [DjangoFilterBackend]


class MonthlyReportViewSet(viewsets.ModelViewSet):
    queryset = MonthlyReport.objects.all()
    serializer_class = MonthlyReportSerializer
    filter_backends = [DjangoFilterBackend]


class CompetitionReportViewSet(viewsets.ModelViewSet):
    queryset = CompetitionReport.objects.all()
    serializer_class = CompetitionReportSerializer
    filter_backends = [DjangoFilterBackend]


class VacationReportViewSet(viewsets.ModelViewSet):
    queryset = VacationReport.objects.all()
    serializer_class = VacationReportSerializer
    filter_backends = [DjangoFilterBackend]