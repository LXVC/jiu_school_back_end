# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from .serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
