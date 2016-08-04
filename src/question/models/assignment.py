# -*- coding:utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, \
    IntegerField, DateTimeField, NullBooleanField, TextField
from django.contrib.auth.models import User
from education.models import Org
from .question import Question
from .question_desc import Charpter


class CodeAssignmentStatus(Model):
    status_name = CharField(max_length=20, default='草稿', verbose_name='状态')

    class Meta:
        app_label = 'question'
        db_table = 'code_assignment_status'
        verbose_name = '作业状态'
        verbose_name_plural = '作业状态'

    def __unicode__(self):
        return u'{0}'.format(self.status_name)


class CodeAssignmentType(Model):
    assignment_type_name = CharField(max_length=50, default='日常作业', verbose_name='类型')

    class Meta:
        app_label = 'question'
        db_table = 'code_assignment_type'
        verbose_name = '作业类型'
        verbose_name_plural = '作业类型'

    def __unicode__(self):
        return u'{0}'.format(self.assignment_type_name)


class Assignment(Model):
    title = CharField(max_length=30, verbose_name='名称')
    questhion_num = IntegerField(default=2, verbose_name='题目数量')
    created_by = ForeignKey(User, db_column='created_by', related_name='created_assignment', verbose_name='创建者')
    charpter = ForeignKey(Charpter, db_column='charpter_id', related_name='assignments', verbose_name='所属章节')
    owner = ForeignKey(Org, db_column='owner', related_name='own_assignments', verbose_name='拥有者')
    status = ForeignKey(CodeAssignmentStatus, db_column='status', verbose_name='状态')
    published_count = IntegerField(default=1, verbose_name='提交数')
    created_date = DateTimeField(auto_now_add=True, verbose_name='创建日期')
    type = ForeignKey(CodeAssignmentType, db_column='type', verbose_name='作业类型')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'assignment'
        verbose_name = '作业'
        verbose_name_plural = '作业'

    def __unicode__(self):
        return u'{0}'.format(self.title)


class AssignmentPublish(Model):
    assignment = ForeignKey(Assignment, db_column='assignment_id', verbose_name='作业')
    publisher = ForeignKey(User, db_column='publisher', verbose_name='提交人')
    reciver_org = ForeignKey(Org, db_column='reciver_org', verbose_name='接收组织')
    share = NullBooleanField(default=False, verbose_name='是否分享')
    publish_date = DateTimeField(blank=True, verbose_name='提交日期')
    publish_date_start = DateTimeField(blank=True, verbose_name='最早提交时间')
    publish_date_end = DateTimeField(blank=True, verbose_name='最晚提交时间')
    comments = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'assignment_publish'
        verbose_name = '作业提交情况'
        verbose_name_plural = '作业提交情况'

    def __unicode__(self):
        return u'{0}——{1}'.format(self.publisher.username, self.assignment.title)


class CodeSubmitStatus(Model):
    stastus = (('未做', '未做'),
               ('完成', '完成'),
               ('草稿', '草稿'),
               ('过期', '过期'),)
    submit_status_name = CharField(max_length=20, choices=stastus, verbose_name='状态')

    class Meta:
        app_label = 'question'
        db_table = 'code_submit_status'
        verbose_name = '作业提交状态'
        verbose_name_plural = '作业提交状态'

    def __unicode__(self):
        return u'{0}'.format(self.submit_status_name)


class AssignmentSubmit(Model):
    assignment_publish = ForeignKey(AssignmentPublish, db_column='assignment_publish_id', verbose_name='作业提交')
    context = TextField(verbose_name='内容')
    submiter = ForeignKey(User, db_column='submiter', verbose_name='提交人')
    status = ForeignKey(CodeSubmitStatus, db_column='status', verbose_name='提交状态')
    start_date = DateTimeField(blank=True, verbose_name='开始时间')
    submit_date = DateTimeField(blank=True, verbose_name='提交时间')
    comment = CharField(max_length=500, blank=True, verbose_name='备注')

    class Meta:
        app_label = 'question'
        db_table = 'assignment_submit'
        verbose_name = '作业提交状态'
        verbose_name_plural = '作业提交状态'

    def __unicode__(self):
        return u'{0}'.format(self.context[:10])


class AssignmentSubmitDetail(Model):
    submit = ForeignKey(AssignmentSubmit, db_column='submit_id', verbose_name='提交')
    question = ForeignKey(Question, db_column='question_id', verbose_name='问题')
    context = CharField(max_length=500, blank=True, verbose_name='答题内容')
    checking_status = CharField(max_length=20, blank=True, verbose_name='批改状态')
    checking_context = CharField(max_length=500, blank=True, verbose_name='批改内容')
    checking_date = DateTimeField(auto_now=True, verbose_name='批改时间')
    checking_by = ForeignKey(User, db_column='checking_by', verbose_name='批改人')
    checking_comments = CharField(max_length=500, blank=True, verbose_name='批改备注')
    status = CharField(max_length=20, blank=True, verbose_name='状态')

    class Meta:
        app_label = 'question'
        db_table = 'assignment_submit_detail'
        verbose_name = '作业详情'
        verbose_name_plural = '作业详情'

    def __unicode__(self):
        return u'{0}--{1}--{2}'.format(self.submit.submiter.username, self.question.content[:10], self.context[:10])
