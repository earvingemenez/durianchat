from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Message

from accounts.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):

    # sender = UserSerializer()
    # recipient = UserSerializer()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'content')


##################################
## SAMPLE OF NON-ORM SERIALIZER ##
##################################
class MessageStaticSerializer(serializers.Serializer):

    sender = serializers.IntegerField()
    recipient = serializers.IntegerField()
    content = serializers.CharField()