from calendar import Calendar
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .serializers import *

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["user"]