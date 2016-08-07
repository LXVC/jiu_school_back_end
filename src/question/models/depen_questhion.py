# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, IntegerField, DateTimeField, SmallIntegerField
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from education.models import Org
from .question import Question


class QuestionsDyndifficulty(Model):
    question = ForeignKey(Question, db_column='question_id', verbose_name='题目')
    diffcultty = IntegerField(default=0, verbose_name='难度等级')
    calc_date = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'questions_dyndifficulty'
        verbose_name = '题目难度'
        verbose_name_plural = '题目难度'

    def __unicode__(self):
        return u'{0}'.format(str(self.diffcultty))


class KnowegePoint(MPTTModel):
    title = CharField(max_length=100, verbose_name='知识点名字')
    parent = TreeForeignKey('self', db_column='parent_id', blank=True, null=True, related_name='children',
                            verbose_name='父知识点')
    ref_count = IntegerField(default=0, verbose_name='引用次数')
    created_by = ForeignKey(User, db_column='created_by', related_name='created_knowege_points', verbose_name='创建者')
    owner = ForeignKey(Org, db_column='owner', related_name='own_knowege_points', verbose_name='拥有者')
    created_date = DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        app_label = 'question'
        db_table = 'knowege_point'
        verbose_name = '知识点'
        verbose_name_plural = '知识点'

    def __unicode__(self):
        return u'{0}'.format(self.title)


class QuestionKnowlegePoint(Model):
    questhion = ForeignKey(Question, db_column='questhion_id', verbose_name='题目')
    index = ForeignKey(KnowegePoint, db_column='index', verbose_name='知识点')

    class Meta:
        app_label = 'question'
        db_table = 'question_knowlege_point'
        verbose_name = '题目和知识点对应关系'
        verbose_name_plural = '题目和知识点对应关系'

    def __unicode__(self):
        return u'{0}...——{1}'.format(self.questhion.content[:5], self.index.title)


class WeakPoint(Model):
    user = ForeignKey(User, db_column='user_id', verbose_name='学生')
    question = ForeignKey(Question, db_column='question_id', verbose_name='题目')

    class Meta:
        app_label = 'question'
        db_table = 'weak_point'
        verbose_name = '学生的薄弱知识'
        verbose_name_plural = '学生的薄弱知识'

    def __unicode__(self):
        return u'{0}——{1}'.format(self.user.username, self.question.content[:10])
