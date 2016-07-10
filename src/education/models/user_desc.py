# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, ForeignKey
from .user import User


class CodeRole(Model):
    # 用户身份表
    id = IntegerField(primary_key=True)
    role_name = CharField(max_length=20)
    comments = CharField(max_length=500)

    class Meta:
        app_label = 'education'
        db_table = 'code_role'


class CodeAccountType(Model):
    # 用户账户类型表
    id = IntegerField(primary_key=True)
    acc_type_name = CharField(max_length=20)
    comments = CharField(max_length=500)

    class Meta:
        app_label = 'education'
        db_table = 'code_account_type'


class UserPermissions(Model):
    id = IntegerField(primary_key=True)
    user = ForeignKey(User, verbose_name='user_id')
    permission_id = IntegerField()

    class Meta:
        app_label = 'education'
        db_table = 'user_permissions'
