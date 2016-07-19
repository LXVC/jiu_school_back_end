# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from education.api.serializers import UserSerializers


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)


class CreateToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            token = Token.objects.get(user=user)
            token.delete()
        finally:
            token = Token.objects.create(user=user)
            return Response({'token': token.key})
