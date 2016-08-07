# -*- coding:utf-8 -*-
from django.db.models import Model, CharField, IntegerField, ForeignKey, \
    FloatField, SmallIntegerField, DateTimeField
from mptt.models import MPTTModel, TreeForeignKey


class Area(MPTTModel):
    # 地区表
    parent = TreeForeignKey('self', db_column='parent_id', null=True, blank=True, related_name='children',
                            verbose_name='上级')
    # path = CharField(max_length=200, blank=True, verbose_name='具体位置')
    # level = SmallIntegerField(blank=True, default=4, verbose_name='级别')
    name = CharField(max_length=50, blank=True, verbose_name='名称')
    short_name = CharField(max_length=50, blank=True, verbose_name='简称')
    longitude = FloatField(blank=True, default=1.1, null=True, verbose_name='经度')
    latitude = FloatField(blank=True, default=2.2, null=True, verbose_name='纬度')
    sort = IntegerField(blank=True, default=1)
    status = SmallIntegerField(blank=True, default=2, verbose_name='状态')

    class Meta:
        app_label = 'education'
        db_table = 'area'
        verbose_name = '地区'
        verbose_name_plural = '地区'

    def __unicode__(self):
        return u'{0}'.format(self.name)


class CodeEduPeriod(Model):
    # 学段类别表
    edu_period_name = CharField(max_length=20, blank=True, default='中学', verbose_name='学段')

    class Meta:
        app_label = 'education'
        db_table = 'code_edu_period'
        verbose_name = '学段'
        verbose_name_plural = '学段'

    def __unicode__(self):
        return u'{0}'.format(self.edu_period_name)


class CodeGrade(Model):
    grade_name = CharField(max_length=10, verbose_name='年级', blank=True, default='初一')

    class Meta:
        app_label = 'education'
        db_table = 'grades'
        verbose_name = '年级'
        verbose_name_plural = '年级'

    def __unicode__(self):
        return u'{0}'.format(self.grade_name)


class Org(MPTTModel):
    # 组织模型表
    parent = TreeForeignKey('self', db_column='parent_id', null=True, blank=True, related_name='children',
                            verbose_name='上级组织')
    area = ForeignKey(Area, db_column='area_id', verbose_name='地区')
    name = CharField(max_length=50, blank=True, default='XX中学', verbose_name='组织名称')
    edu_period = ForeignKey(CodeEduPeriod, db_column='edu_period', verbose_name='学段')
    size = IntegerField(blank=True, default=1200, verbose_name='总人数')
    # path = CharField(max_length=200, default='湖南', blank=True, verbose_name='具体地址')
    # level = SmallIntegerField(blank=True, default=1, verbose_name='级别')
    type = CharField(max_length=10, default='学校', verbose_name='组织类型')
    sort = IntegerField(blank=True, default=2)
    status = SmallIntegerField(default=0, blank=2, verbose_name='状态')
    created_date = DateTimeField(blank=True, auto_now_add=True, verbose_name='创建日期')
    grade = ForeignKey(CodeGrade, db_column='grade', blank=True, null=True, verbose_name='年级')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'education'
        db_table = 'org'
        verbose_name = '组织'
        verbose_name_plural = '组织'

    def __unicode__(self):
        return u'{0}'.format(self.name)


class KeySchool(Model):
    # 重点学校
    org = ForeignKey(Org, db_column='org_id', verbose_name='学校')
    type = IntegerField(blank=True, default=10, verbose_name='等级')

    class Meta:
        app_label = 'education'
        db_table = 'keyschool'
        verbose_name = '名牌学校'
        verbose_name_plural = '名牌学校'

    def __unicode__(self):
        return u'{0}-{1}'.format(self.org.name, self.type)
