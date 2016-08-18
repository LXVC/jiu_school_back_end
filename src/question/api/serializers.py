# -*- coding:utf-8 -*-
from rest_framework import serializers

from education.utils import convert_timezone

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
    class Meta:
        model = models.Assignment
        fields = ('id', 'title')


class AssignmentPublishSerializers(serializers.ModelSerializer):
    assignment_name = serializers.ReadOnlyField(source='assignment.title')
    assignment_id = serializers.ReadOnlyField(source='assignment.id')
    publish_date = serializers.SerializerMethodField()

    class Meta:
        model = models.AssignmentPublish
        fields = ('id', 'assignment_name', 'assignment_id', 'publish_date')

    def get_publish_date(self, obj):
        return convert_timezone(obj.publish_date)


class AssignmentDetailsSerializers(serializers.ModelSerializer):
    assignment_id = serializers.ReadOnlyField(source='assignment.id')
    question_id = serializers.ReadOnlyField(source='question.id')
    question_content = serializers.ReadOnlyField(source='question.content')

    class Meta:
        model = models.AssignmentQuestions
        fields = ('id', 'assignment_id', 'question_id', 'question_content')
