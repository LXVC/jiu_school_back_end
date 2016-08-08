# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from education.models import Profile, Org, Notice, \
    NoticeTo, UserOrg, Version, KeyTeacher, KeySchool
from education.api.serializers import UserSerializers, ProfileSerializers, \
    OrgSerializers, NoticeSerializers, VersionSerializers, KeyTeacherSerializers, KeySchoolSerializers
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
        notices_to_org = []
        notices_to_user = NoticeTo.objects.filter(user=request.user)
        for i in notices_to_user:
            user_notice.append(i.notice)
        user_orgs = UserOrg.objects.filter(user=request.user)
        for j in user_orgs:
            tem = NoticeTo.objects.filter(org=j.org)
            for t in tem:
                notices_to_org.append(t.notice)
        all_notice = user_notice + notices_to_org
        for notice in all_notice:
            notice.created_date = convert_timezone(notice.created_date)
        serializer = NoticeSerializers(set(all_notice), many=True)
        return Response(serializer.data)


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializers

    def list(self, request, *args, **kwargs):
        queryset = Version.objects.all().last()
        serializer = VersionSerializers(queryset)
        return Response(serializer.data)


class KeyTeacherViewSet(viewsets.ModelViewSet):
    queryset = KeyTeacher.objects.all()
    serializer_class = KeyTeacherSerializers


class KeySchoolViewSet(viewsets.ModelViewSet):
    queryset = KeySchool.objects.all()
    serializer_class = KeySchoolSerializers
