from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


class CreateMessageAPI(APIView):
    """ Create message object
    """
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = MessageSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetailAPI(APIView):
    """ Retrieve, Update, or delete a message instance
    """
    def get_object(self, message_id):
        try:
            return Message.objects.get(id=message_id)
        except Message.DoesNotExist as e:
            # log e
            # Raise error
            raise Http404

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


