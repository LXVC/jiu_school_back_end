# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from education.models import Profile, Org, Notice


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


class ProfileSerializers(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.name')
    org = serializers.ReadOnlyField(source='org.name')

    class Meta:
        model = Profile
        fields = ('user', 'email', 'org')


class OrgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ('pk', 'name',)


class NoticeSerializers(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Notice
        field = ('title', 'created_by', 'created_date', 'content')
