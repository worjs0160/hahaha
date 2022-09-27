from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Messenger
from .serializers import MessengerSerializer
from django_filters import rest_framework as filters


class MessengerViewSet(viewsets.ModelViewSet):
    queryset = Messenger.objects.all()
    serializer_class = MessengerSerializer
    
