# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, EmailField, ForeignKey, DateTimeField, OneToOneField
from .user import Profile
from .user_desc import CodeUserStatus
from django.contrib.auth.models import Permission, Group


class UserPermissions(Model):
    # 用户权限表
    user = ForeignKey(Profile, db_column='user_id', verbose_name='用户')
    permission = ForeignKey(Permission, db_column='permission_id', default=1, verbose_name='权限')

    class Meta:
        app_label = 'education'
        db_table = 'user_permissions'
        verbose_name = '用户与权限'
        verbose_name_plural = '用户与权限'

    def __unicode__(self):
        return u'{0}-{1}'.format(self.user.user.username, self.permission.codename)


class UserRelationInfo(Model):
    # 用户亲属关系表
    user = OneToOneField(Profile, primary_key=True, db_column='user_id', verbose_name='用户')
    relation_type = CharField(max_length=10, default='父亲', blank=True, verbose_name='关系')
    relation_name = CharField(max_length=50, default='李天一', blank=True, verbose_name='姓名')
    relation_phone = CharField(max_length=32, default='13788740727', verbose_name='手机号')
    relation_email = EmailField(blank=True, default='403381161@qq.com', verbose_name='邮箱')
    relation_address = CharField(max_length=200, default='湖南', verbose_name='家庭住址')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'education'
        db_table = 'user_relation_info'
        verbose_name = '用户亲属关系'
        verbose_name_plural = '用户亲属关系'

    def __unicode__(self):
        return u'{0}-{1}-{2}'.format(self.user.username, self.relation_type, self.relation_name)


class UserStatusChangeLog(Model):
    # 用户状态变化表
    user = ForeignKey(Profile, db_column='user_id', related_name='statusChange')
    old_status = ForeignKey(CodeUserStatus, db_column='old_status', related_name='old')
    new_status = ForeignKey(CodeUserStatus, db_column='new_status', related_name='new')
    change_date = DateTimeField(blank=True)
    resason = CharField(max_length=500, default='我喜欢')
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
