from rest_framework import serializers
from .models import Messenger
from users.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name"]

class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messenger
        fields = ["user", "message", "roomNum"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = UserSerializer(instance.user).data
        return response