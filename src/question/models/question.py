# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, TextField, DateTimeField,\
                            SmallIntegerField, NullBooleanField, CharField
from django.contrib.auth.models import User
from .question_desc import Charpter, CodeQuesthionType, CodeContextType,Library


class Question(Model):
    ref = ForeignKey('self', db_column='ref_id', null=True, blank=True)
    charpter = ForeignKey(Charpter, db_column='charpter_id')
    content = TextField()
    type = ForeignKey(CodeQuesthionType, db_column='type')
    owner = ForeignKey(User, db_column='owner', related_name='questions')
    answer = TextField()
    answer_type = ForeignKey(CodeContextType, db_column='answer_type')
    difficultly = SmallIntegerField(default=1)
    kp = TextField()
    solve = TextField()
    created_date = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(User, db_column='created_by', related_name='created_questions')
    edit_by = ForeignKey(User, db_column='edit_by', related_name='edited_questions')
    status = SmallIntegerField(default=1)
    share = NullBooleanField(null=True)
    library = ForeignKey(Library, db_column='library_id')
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'questions'


class Material(Model):
    ref = ForeignKey('self', db_column='ref_id', null=True, blank=True)
    content = TextField(blank=True)
    created_by = ForeignKey(User, related_name='created_materials', db_column='created_by')
    edit_by = ForeignKey(User, related_name='edited_materials', db_column='edit_by', null=True)
    created_date = DateTimeField(auto_now_add=True)
    comments = TextField(blank=True)

    class Meta:
        app_label = 'question'
        db_table = 'materials'
