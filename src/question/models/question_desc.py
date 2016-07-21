# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, BooleanField, SmallIntegerField
from education.models import Org


class Library(Model):
    library_name = CharField(max_length=100)
    public = BooleanField(default=False)
    owner = ForeignKey(Org, db_column='owner')

    class Meta:
        app_label = 'question'
        db_table = 'library'


class CodeQuesthionType(Model):
    questhion_type_name = CharField(max_length=20)

    class Meta:
        app_label = 'question'
        db_table = 'code_questhion_type'


class CodeContextType(Model):
    context_type_name = CharField(max_length=20)

    class Meta:
        app_label = 'question'
        db_table = 'code_context_type'


class CodeSubject(Model):
    sujects = (('语文', '语文'),
               ('数学', '数学'),
               ('英语', '英语'),
               ('物理', '物理'),
               ('化学', '化学'),
               ('生物', '生物'),
               ('历史', '历史'),
               ('地理', '地理'),
               ('政治', '政治'),)
    subject_name = CharField(max_length=20, choices=sujects)

    class Meta:
        app_label = 'question'
        db_table = 'code_subject'


class Charpter(Model):
    title = CharField(max_length=200)
    subject = ForeignKey(CodeSubject, db_column='subject')
    parent = ForeignKey('self', null=True, blank=True, db_column='parent_id')
    path = CharField(max_length=200)
    level = SmallIntegerField(default=0)
    owner = ForeignKey(Org, db_column='owner')
    comment = CharField(max_length=500)

    class Meta:
        app_label = 'question'
        db_table = 'charpter'
