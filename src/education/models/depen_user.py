# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, EmailField, ForeignKey, OneToOneField
from .user import User


class UserPermissions(Model):
    # 用户权限表
    id = IntegerField(primary_key=True)
    user_id = ForeignKey(User, db_column='user_id')
    permission_id = IntegerField()

    class Meta:
        app_label = 'education'
        db_table = 'user_permissions'


class UserRelationInfo(Model):
    # 用户亲属关系表
    user_id = OneToOneField(User, primary_key=True, db_column='user_id')
    relation_type = CharField(max_length=10)
    relation_name = CharField(max_length=50)
    relation_phone = CharField(max_length=32)
    relation_email = EmailField()
    relation_address = CharField(max_length=200)
    comments = CharField(max_length=500)

    class Meta:
        app_label = 'education'
        db_table = 'user_relation_info'
