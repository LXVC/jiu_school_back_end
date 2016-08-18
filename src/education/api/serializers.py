# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from education import models


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # write_only_fields = ('password',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializers, self).update(instance, validated_data)


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = models.Profile
        fields = ('user', 'email')


class OrgSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Org
        fields = ('pk', 'name',)


class NoticeSerializers(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = models.Notice
        fields = ('title', 'created_by', 'created_date', 'content')


class VersionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Version
        fields = ('version', 'url', 'comments', 'created_date')
        read_only_fields = ('version', 'url', 'comments', 'created_date')


class KeyTeacherSerializers(serializers.ModelSerializer):
    teacher_name = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = models.KeyTeacher
        fields = ('teacher_name', 'details')


class KeySchoolSerializers(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='org.name')

    class Meta:
        model = models.KeySchool
        fields = ('school_name', 'type')


class UserOrgSerializers(serializers.ModelSerializer):
    org_name = serializers.ReadOnlyField(source='org.name')
    org_id = serializers.ReadOnlyField(source='org.id')

    class Meta:
        model = models.UserOrg
        fields = ('id', 'org_name', 'org_id')
