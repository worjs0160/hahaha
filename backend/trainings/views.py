import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from .models import *
from .serializers import *
from .filters import *


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TrainingFilter


class TrainingUserViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter()
    serializer_class = TrainingUserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "comID", "userType"]


class CreateImageViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = TrainingImage.objects.all()
    serializer_class = TrainingImageSerializer


class CCTrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = CCTrainingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TrainingFilter