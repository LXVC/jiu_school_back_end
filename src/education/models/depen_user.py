# -*- coding:utf-8 -*-

from django.db.models import Model, CharField, EmailField, ForeignKey, DateTimeField, OneToOneField
from .user import Profile
from .user_desc import CodeUserStatus
from django.contrib.auth.models import Permission,Group


class UserPermissions(Model):
    # 用户权限表
    user = ForeignKey(Profile, db_column='user_id')
    permission = ForeignKey(Permission, db_column='permission_id', default=0)

    class Meta:
        app_label = 'education'
        db_table = 'user_permissions'


class UserRelationInfo(Model):
    # 用户亲属关系表
    user = OneToOneField(Profile, primary_key=True, db_column='user_id')
    relation_type = CharField(max_length=10)
    relation_name = CharField(max_length=50)
    relation_phone = CharField(max_length=32)
    relation_email = EmailField()
    relation_address = CharField(max_length=200)
    comments = CharField(max_length=500, blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'user_relation_info'


class UserStatusChangeLog(Model):
    # 用户状态变化表
    user = ForeignKey(Profile, db_column='user_id')
    old_status = ForeignKey(CodeUserStatus, db_column='old_status', related_name='old_status')
    new_status = ForeignKey(CodeUserStatus, db_column='new_status', related_name='new_status')
    change_date = DateTimeField()
    resason = CharField(max_length=500)
    oper = ForeignKey(Profile, db_column='oper', related_name='operator')

    class Meta:
        app_label = 'education'
        db_table = 'user_status_change_log'


class UserGroup(Model):
    # 用户权限组关系表
    user = ForeignKey(Profile, db_column='user_id')
    group = ForeignKey(Group, db_column='group_id')

    class Meta:
        app_label = 'education'
        db_table = 'user_group'
