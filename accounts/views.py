from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .mixins import UserMixin


class UserAPIView(UserMixin, APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        # serialize user object
        serializer = UserSerializer(self.request.user)
        
        return Response(serializer.data)


class UserListAPIView(UserMixin, APIView):

    def get(self, *args, **kwargs):
        # Serializer all Users
        serializer = UserSerializer(self.queryset, many=True)

        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(data['password'])
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


class UserDetailAPIView(UserMixin, APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.get_object(kwargs.get('user_id'))
        # serialize user object
        serializer = UserSerializer(user)

        return Response(serializer.data)