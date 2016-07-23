# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, ForeignKey, DateTimeField, TextField, BooleanField
from django.contrib.auth.models import User
from .org import Org


class Notice(Model):
    title = CharField(max_length=20)
    created_by = ForeignKey(User, db_column='create_by', related_name='created_notices')
    created_date = DateTimeField(auto_now_add=True)
    content = TextField()

    class Meta:
        app_label = 'education'
        db_table = 'notices'


class NoticeTo(Model):
    notice = ForeignKey(Notice, db_column='notice_id')
    user = ForeignKey(User, db_column='user_id', null=True, related_name='notices', blank=True)
    org = ForeignKey(Org, db_column='org_id', null=True, related_name='notices', blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'notice_to'
