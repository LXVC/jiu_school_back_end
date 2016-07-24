# -*- coding:utf-8 -*-
from django.db.models import Model, CharField


class CodeRole(Model):
    # 用户角色表
    role_name = CharField(max_length=20, blank=True, default=u'学生', verbose_name='身份')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'education'
        db_table = 'code_role'
        verbose_name = '用户身份'
        verbose_name_plural = '用户身份'

    def __unicode__(self):
        return u'{0}'.format(self.role_name)


class CodeAccountType(Model):
    # 用户账户类型表
    acc_type_name = CharField(max_length=20, default=u'手机号', verbose_name='帐号类型')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'education'
        db_table = 'code_account_type'
        verbose_name = '用户账号类型'
        verbose_name_plural = '用户账号类型'

    def __unicode__(self):
        return u'{0}'.format(self.acc_type_name)


class CodeUserStatus(Model):
    # 账户状态表
    user_state_name = CharField(max_length=20, default=u'在线', verbose_name='状态')

    class Meta:
        app_label = 'education'
        db_table = 'code_user_status'
        verbose_name = '用户帐号状态'
        verbose_name_plural = '用户帐号状态'

    def __unicode__(self):
        return u'{0}'.format(self.user_state_name)
