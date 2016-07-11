# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, EmailField, ForeignKey, DateTimeField, OneToOneField
from .user import User
from .user_desc import CodeUserStatus


class UserPermissions(Model):
    # 用户权限表
    user = ForeignKey(User, db_column='user_id')
    permission = IntegerField(db_column='permission_id', default=0)

    class Meta:
        app_label = 'education'
        db_table = 'user_permissions'


class UserRelationInfo(Model):
    # 用户亲属关系表
    user = OneToOneField(User, primary_key=True, db_column='user_id')
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
    use = ForeignKey(User, db_column='user_id', related_name='who')
    old_status = ForeignKey(CodeUserStatus, db_column='old_status', related_name='old_status')
    new_status = ForeignKey(CodeUserStatus, db_column='new_status', related_name='new_status')
    change_date = DateTimeField()
    resason = CharField(max_length=500)
    oper = ForeignKey(User, db_column='oper', related_name='operator')

    class Meta:
        app_label = 'education'
        db_table = 'user_status_change_log'

