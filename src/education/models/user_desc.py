# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, AutoField


class CodeRole(Model):
    # 用户角色表
    role_name = CharField(max_length=20)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'code_role'


class CodeAccountType(Model):
    # 用户账户类型表
    acc_type_name = CharField(max_length=20)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'code_account_type'


class CodeUserStatus(Model):
    # 账户状态表
    user_state_name = CharField(max_length=20)

    class Meta:
        app_label = 'education'
        db_table = 'code_user_status'
