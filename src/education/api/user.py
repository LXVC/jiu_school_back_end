# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from education.models import Profile, Org, Notice, NoticeTo
from education.api.serializers import UserSerializers, ProfileSerializers, OrgSerializers, NoticeSerializers
from education.utils import convert_timezone


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
            return Response({'token': token.key,
                             'id': token.user_id})


class UsersProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


class OrgViewSet(viewsets.ModelViewSet):
    queryset = Org.objects.all()
    serializer_class = OrgSerializers


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers

    def list(self, request, *args, **kwargs):
        user_notice = []
        org_notice = []
        notices_to_org = []
        notices_to_user = NoticeTo.objects.filter(user=request.user)
        try:
            org = Profile.objects.get(user=request.user).org
            notices_to_org = NoticeTo.objects.filter(org=org)
        except Profile.DoesNotExist:
            print('this user no Profile')
        for i in notices_to_user:
            i.notice.created_date = convert_timezone(i.notice.created_date)
            user_notice.append(i.notice)
        for j in notices_to_org:
            j.notice.created_date = convert_timezone(j.notice.created_date)
            org_notice.append(j.notice)
        all_notice = user_notice + org_notice
        serializer = NoticeSerializers(all_notice, many=True)
        return Response(serializer.data)
