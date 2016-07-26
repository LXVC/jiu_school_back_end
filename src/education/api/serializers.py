# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from education.models import Profile, Org, Notice, Version


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
        print('rest password')
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializers, self).update(instance, validated_data)


class ProfileSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = Profile
        fields = ('user', 'email')


class OrgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = ('pk', 'name',)


class NoticeSerializers(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Notice
        fields = ('title', 'created_by', 'created_date', 'content')


class VersionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('version', 'url', 'comments', 'created_date')
        read_only_fields = ('version', 'url', 'comments', 'created_date')
