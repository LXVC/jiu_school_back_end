# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, ForeignKey, DateTimeField, TextField, BooleanField
from django.contrib.auth.models import User
from .org import Org


class Notice(Model):
    title = CharField(max_length=20, verbose_name='主题')
    created_by = ForeignKey(User, db_column='create_by', related_name='created_notices', verbose_name='发布人')
    created_date = DateTimeField(auto_now_add=True, verbose_name='创建日期')
    content = TextField(verbose_name='内容')

    class Meta:
        app_label = 'education'
        db_table = 'notices'
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __unicode__(self):
        return u'{0}'.format(self.title)


class NoticeTo(Model):
    notice = ForeignKey(Notice, db_column='notice_id')
    user = ForeignKey(User, db_column='user_id', null=True, related_name='notices', blank=True)
    org = ForeignKey(Org, db_column='org_id', null=True, related_name='notices', blank=True)

    class Meta:
        app_label = 'education'
        db_table = 'notice_to'
        verbose_name = '公告接收人或者组织'
        verbose_name_plural = '公告接收人或者组织'

    def __unicode__(self):
        to = self.user or self.org
        if isinstance(to, User):
            to = self.user.username
        else:
            to = self.org.name
        return u'「{0}」To「{1}」'.format(self.notice.title, to)
