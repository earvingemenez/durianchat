from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Message


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class MessageSerializer(serializers.ModelSerializer):

    sender = UserSerializer()
    recipient = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'content')