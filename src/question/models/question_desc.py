# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, BooleanField, SmallIntegerField
from education.models import Org


class Library(Model):
    library_name = CharField(max_length=100, verbose_name='名字')
    public = BooleanField(default=False, verbose_name='是否公开')
    owner = ForeignKey(Org, db_column='owner', verbose_name='拥有者')

    class Meta:
        app_label = 'question'
        db_table = 'library'
        verbose_name = '图书馆'
        verbose_name_plural = '图书馆'

    def __unicode__(self):
        return u'{0}'.format(self.library_name)


class CodeQuesthionType(Model):
    type = ((u'主观题', u'主观题'),
            (u'客观题', u'客观题'))
    questhion_type_name = CharField(max_length=20, verbose_name='题目类型', choices=type)

    class Meta:
        app_label = 'question'
        db_table = 'code_questhion_type'
        verbose_name = '题目类型'
        verbose_name_plural = '题目类型'

    def __unicode__(self):
        return u'{0}'.format(self.questhion_type_name)


class CodeContextType(Model):
    type = ((u'文字', u'文字'),
            (u'图片', u'图片'))
    context_type_name = CharField(max_length=20, verbose_name='答案类型', choices=type)

    class Meta:
        app_label = 'question'
        db_table = 'code_context_type'
        verbose_name = '答案类型'
        verbose_name_plural = '答案类型'

    def __unicode__(self):
        return u'{0}'.format(self.context_type_name)


class CodeSubject(Model):
    sujects = ((u'语文', u'语文'),
               (u'数学', u'数学'),
               (u'英语', u'英语'),
               (u'物理', u'物理'),
               (u'化学', u'化学'),
               (u'生物', u'生物'),
               (u'历史', u'历史'),
               (u'地理', u'地理'),
               (u'政治', u'政治'),)
    subject_name = CharField(max_length=20, choices=sujects, verbose_name='科目')

    class Meta:
        app_label = 'question'
        db_table = 'code_subject'
        verbose_name = '科目'
        verbose_name_plural = '科目'

    def __unicode__(self):
        return u'{0}'.format(self.subject_name)


class Charpter(Model):
    title = CharField(max_length=200, verbose_name='章节')
    subject = ForeignKey(CodeSubject, db_column='subject', verbose_name='科目')
    parent = ForeignKey('self', null=True, blank=True, db_column='parent_id', verbose_name='父章节')
    path = CharField(max_length=200, verbose_name='位置')
    level = SmallIntegerField(default=0, verbose_name='级别')
    owner = ForeignKey(Org, db_column='owner', verbose_name='拥有者')
    comment = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'charpter'
        verbose_name = '章节'
        verbose_name_plural = '章节'

    def __unicode__(self):
        return u'{0}'.format(self.title)
