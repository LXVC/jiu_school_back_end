# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, BooleanField, SmallIntegerField
from mptt.models import MPTTModel, TreeForeignKey
from education.models import Org


class Library(Model):
    library_name = CharField(max_length=100, verbose_name='名字')
    public = BooleanField(default=False, verbose_name='是否公开')
    owner = ForeignKey(Org, db_column='owner', related_name='owner_librarys', verbose_name='拥有者')

    class Meta:
        app_label = 'question'
        db_table = 'library'
        verbose_name = '题库'
        verbose_name_plural = '题库'

    def __unicode__(self):
        return u'{0}'.format(self.library_name)


class CodeQuesthionType(Model):
    questhion_type_name = CharField(max_length=20, verbose_name='题目类型')

    class Meta:
        app_label = 'question'
        db_table = 'code_questhion_type'
        verbose_name = '题目类型'
        verbose_name_plural = '题目类型'

    def __unicode__(self):
        return u'{0}'.format(self.questhion_type_name)


class CodeContextType(Model):
    context_type_name = CharField(max_length=20, verbose_name='答案类型')

    class Meta:
        app_label = 'question'
        db_table = 'code_context_type'
        verbose_name = '答案类型'
        verbose_name_plural = '答案类型'

    def __unicode__(self):
        return u'{0}'.format(self.context_type_name)


class CodeSubject(Model):
    subject_name = CharField(max_length=20, verbose_name='科目')

    class Meta:
        app_label = 'question'
        db_table = 'code_subject'
        verbose_name = '科目'
        verbose_name_plural = '科目'

    def __unicode__(self):
        return u'{0}'.format(self.subject_name)


class Charpter(MPTTModel):
    title = CharField(max_length=200, verbose_name='章节')
    subject = ForeignKey(CodeSubject, db_column='subject', verbose_name='科目')
    parent = TreeForeignKey('self', null=True, blank=True, db_column='parent_id', verbose_name='父章节',
                            related_name='children')
    # path = CharField(max_length=200, verbose_name='位置')
    # level = SmallIntegerField(default=0, verbose_name='级别')
    owner = ForeignKey(Org, db_column='owner', verbose_name='拥有者')
    comment = CharField(max_length=500, blank=True, default='', verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'charpter'
        verbose_name = '章节'
        verbose_name_plural = '章节'

    def __unicode__(self):
        return u'{0}'.format(self.title)
