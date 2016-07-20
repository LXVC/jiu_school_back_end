# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, IntegerField, DateTimeField
from .question import Question
from django.contrib.auth.models import User


class QuestionsDyndifficulty(Model):
    question = ForeignKey(Question, db_column='question_id')
    diffcultty = IntegerField(default=0)
    calc_date = DateTimeField(auto_now_add=True)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'questions_dyndifficulty'


class KnowegePoint(Model):
    idx = CharField(primary_key=True, max_length=100)
    title = CharField(max_length=100)
    ref_count = IntegerField()
    created_by = ForeignKey(User, db_column='created_by')
    owner = ForeignKey(User, db_column='owner', related_name='knowege_points')
    created_date = DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'question'
        db_table = 'knowege_point'


class QuestionKnowlegePoint(Model):
    questhion = ForeignKey(Question, db_column='questhion_id')
    index = ForeignKey(KnowegePoint, db_column='index')

    class Meta:
        app_label = 'question'
        db_table = 'question_knowlege_point'


class WeakPoint(Model):
    user = ForeignKey(User, db_column='user_id')
    question = ForeignKey(Question, db_column='question_id')

    class Meta:
        app_label = 'question'
        db_table = 'weak_point'
