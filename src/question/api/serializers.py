# -*- coding:utf-8 -*-
from rest_framework import serializers

from question import models


class CharpterSerializers(serializers.ModelSerializer):
    children_details = serializers.SerializerMethodField()

    class Meta:
        model = models.Charpter
        fields = ('id', 'title', 'subject', 'parent', 'owner',
                  'comment', 'children', 'level', 'children_details')

    def get_children_details(self, obj):
        return obj.get_children_details()


class AssignmentSerializers(serializers.ModelSerializer):
    assignment_name = serializers.ReadOnlyField(source='assignment.title')
    assignment_id = serializers.ReadOnlyField(source='assignment.id')

    class Meta:
        model = models.AssignmentPublish
        fields = ('id', 'assignment_name', 'assignment_id')
