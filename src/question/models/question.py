# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, TextField, DateTimeField, \
    SmallIntegerField, NullBooleanField, CharField
from django.contrib.auth.models import User
from .question_desc import Charpter, CodeQuesthionType, CodeContextType, Library
from education.models import Org


class Question(Model):
    ref = ForeignKey('self', db_column='ref_id', blank=True,
                     null=True, related_name='distortion', verbose_name='原题')
    charpter = ForeignKey(Charpter, db_column='charpter_id', related_name='questions', verbose_name='归属章节')
    content = TextField(verbose_name='题目内容')
    type = ForeignKey(CodeQuesthionType, db_column='type', related_name='questions', verbose_name='题目类型')
    owner = ForeignKey(Org, db_column='owner', related_name='own_questions', verbose_name='所有人')
    answer = TextField(blank=True, default='', verbose_name='回答')
    answer_type = ForeignKey(CodeContextType, db_column='answer_type', verbose_name='答题类型')
    difficultly = SmallIntegerField(default=1, verbose_name='难度')
    solve = TextField(blank=True, default='', verbose_name='解析')
    created_date = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(User, db_column='created_by', related_name='created_questions', verbose_name='创建者')
    edit_by = ForeignKey(User, db_column='edit_by', related_name='edited_questions',
                         null=True, blank=True, verbose_name='编辑者')
    status = SmallIntegerField(default=1, verbose_name='状态')
    share = NullBooleanField(null=True, default=False, verbose_name='是否可以分享')
    library = ForeignKey(Library, db_column='library_id', verbose_name='图书馆')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'questions'
        verbose_name = '题目'
        verbose_name_plural = '题目'

    def __unicode__(self):
        return u'{0}...'.format(self.content[:10])


class Material(Model):
    ref = ForeignKey('self', db_column='ref_id', null=True, blank=True, verbose_name='原材料')
    title = CharField(max_length=20, blank=True, verbose_name='标题')
    content = TextField(verbose_name='正文')
    created_by = ForeignKey(User, related_name='created_materials', db_column='created_by', verbose_name='创建者')
    edit_by = ForeignKey(User, related_name='edited_materials', db_column='edit_by', null=True, verbose_name='编辑者')
    created_date = DateTimeField(auto_now_add=True, verbose_name='创建日期')
    comments = TextField(blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'materials'
        verbose_name = '材料'
        verbose_name_plural = '材料'

    def __unicode__(self):
        return u'{0}'.format(self.title)
