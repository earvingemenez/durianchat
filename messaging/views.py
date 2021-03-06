from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .mixins import MessageMixin
from .models import Message
from .serializers import MessageSerializer, MessageStaticSerializer


class MessageListAPI(MessageMixin, APIView):
    """ Create message object
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        # Serialize all message data
        serializer = MessageSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = MessageSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetailAPI(MessageMixin, APIView):
    """ Retrieve, Update, or delete a message instance
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        # Get message id
        message_id = kwargs.get('message_id')
        # Get message object
        message = self.get_object(message_id)
        # Serialize the message object
        serializer = MessageSerializer(message)

        return Response(serializer.data)

    def put(self, *args, **kwargs):
        # Get PUT data
        data = self.request.data
        # Get message id
        message_id = kwargs.get('message_id')
        # Get message object
        message = self.get_object(message_id)
        # Serialize the message object
        serializer = MessageSerializer(message, data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        # Get message id
        message_id = kwargs.get('message_id')
        # Get message object
        message = self.get_object(message_id)
        # Serialize the message object
        message.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



###########################
## Non-class based views ##
###########################
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .models import Message


@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def message_list(request):

    if request.method == "GET":
        # Get all messages
        messages = Message.objects.all()
        # serialize data
        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        # serialize data
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def message_detail(request, message_id):

    # Get message object
    try:
        message = Message.objects.get(id=message_id)
    except Message.DoesNotExist as e:
        return Response(str(e), status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MessageSerializer(message)

        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



##################################
## SAMPLE OF NON-ORM SERIALIZER ##
##################################

class MessageStaticSerializer(APIView):
    """ Serialize data without using a database model.
    """
    def get(self, *args, **kwargs):
        # data from the client
        data = self.request.data
        serializer = MessageStaticSerializer(data)

        # Static data
        message = MessageClass(sender=1, recipient=2, context="Hey there!")
        serializer = MessageStaticSerializer(message)

        return Response(serializer.data)