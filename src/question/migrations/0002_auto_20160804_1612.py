# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignment',
            options={'verbose_name': '\u4f5c\u4e1a', 'verbose_name_plural': '\u4f5c\u4e1a'},
        ),
        migrations.AlterModelOptions(
            name='assignmentpublish',
            options={'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u60c5\u51b5', 'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u60c5\u51b5'},
        ),
        migrations.AlterModelOptions(
            name='assignmentsubmit',
            options={'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001', 'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001'},
        ),
        migrations.AlterModelOptions(
            name='assignmentsubmitdetail',
            options={'verbose_name': '\u4f5c\u4e1a\u8be6\u60c5', 'verbose_name_plural': '\u4f5c\u4e1a\u8be6\u60c5'},
        ),
        migrations.AlterModelOptions(
            name='charpter',
            options={'verbose_name': '\u7ae0\u8282', 'verbose_name_plural': '\u7ae0\u8282'},
        ),
        migrations.AlterModelOptions(
            name='codeassignmentstatus',
            options={'verbose_name': '\u4f5c\u4e1a\u72b6\u6001', 'verbose_name_plural': '\u4f5c\u4e1a\u72b6\u6001'},
        ),
        migrations.AlterModelOptions(
            name='codeassignmenttype',
            options={'verbose_name': '\u4f5c\u4e1a\u7c7b\u578b', 'verbose_name_plural': '\u4f5c\u4e1a\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='codecontexttype',
            options={'verbose_name': '\u7b54\u6848\u7c7b\u578b', 'verbose_name_plural': '\u7b54\u6848\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='codequesthiontype',
            options={'verbose_name': '\u9898\u76ee\u7c7b\u578b', 'verbose_name_plural': '\u9898\u76ee\u7c7b\u578b'},
        ),
        migrations.AlterModelOptions(
            name='codesubject',
            options={'verbose_name': '\u79d1\u76ee', 'verbose_name_plural': '\u79d1\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='codesubmitstatus',
            options={'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001', 'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001'},
        ),
        migrations.AlterModelOptions(
            name='knowegepoint',
            options={'verbose_name': '\u77e5\u8bc6\u70b9', 'verbose_name_plural': '\u77e5\u8bc6\u70b9'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': '\u56fe\u4e66\u9986', 'verbose_name_plural': '\u56fe\u4e66\u9986'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': '\u6750\u6599', 'verbose_name_plural': '\u6750\u6599'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u9898\u76ee', 'verbose_name_plural': '\u9898\u76ee'},
        ),
        migrations.AlterModelOptions(
            name='questionknowlegepoint',
            options={'verbose_name': '\u9898\u76ee\u548c\u77e5\u8bc6\u70b9\u5bf9\u5e94\u5173\u7cfb', 'verbose_name_plural': '\u9898\u76ee\u548c\u77e5\u8bc6\u70b9\u5bf9\u5e94\u5173\u7cfb'},
        ),
        migrations.AlterModelOptions(
            name='questionsdyndifficulty',
            options={'verbose_name': '\u9898\u76ee\u96be\u5ea6', 'verbose_name_plural': '\u9898\u76ee\u96be\u5ea6'},
        ),
        migrations.AlterModelOptions(
            name='weakpoint',
            options={'verbose_name': '\u5b66\u751f\u7684\u8584\u5f31\u77e5\u8bc6', 'verbose_name_plural': '\u5b66\u751f\u7684\u8584\u5f31\u77e5\u8bc6'},
        ),
        migrations.AddField(
            model_name='material',
            name='title',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='charpter',
            field=models.ForeignKey(related_name='assignments', db_column=b'charpter_id', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xab\xa0\xe8\x8a\x82', to='question.Charpter'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_by',
            field=models.ForeignKey(related_name='created_assignment', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='owner',
            field=models.ForeignKey(related_name='own_assignments', db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='published_count',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='questhion_num',
            field=models.IntegerField(default=2, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', to='question.CodeAssignmentStatus'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='title',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='type',
            field=models.ForeignKey(db_column=b'type', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeAssignmentType'),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='assignment',
            field=models.ForeignKey(db_column=b'assignment_id', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a', to='question.Assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='publish_date',
            field=models.DateTimeField(verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='publish_date_end',
            field=models.DateTimeField(verbose_name=b'\xe6\x9c\x80\xe6\x99\x9a\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='publish_date_start',
            field=models.DateTimeField(verbose_name=b'\xe6\x9c\x80\xe6\x97\xa9\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='publisher',
            field=models.ForeignKey(db_column=b'publisher', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='reciver_org',
            field=models.ForeignKey(db_column=b'reciver_org', verbose_name=b'\xe6\x8e\xa5\xe6\x94\xb6\xe7\xbb\x84\xe7\xbb\x87', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='assignmentpublish',
            name='share',
            field=models.NullBooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\x86\xe4\xba\xab'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='assignment_publish',
            field=models.ForeignKey(db_column=b'assignment_publish_id', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x8f\x90\xe4\xba\xa4', to='question.AssignmentPublish'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='comment',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='context',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='start_date',
            field=models.DateTimeField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe7\x8a\xb6\xe6\x80\x81', to='question.CodeSubmitStatus'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='submit_date',
            field=models.DateTimeField(verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmit',
            name='submiter',
            field=models.ForeignKey(db_column=b'submiter', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='checking_by',
            field=models.ForeignKey(db_column=b'checking_by', verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='checking_comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='checking_context',
            field=models.CharField(max_length=500, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='checking_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='checking_status',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='context',
            field=models.CharField(max_length=500, verbose_name=b'\xe7\xad\x94\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='question',
            field=models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='status',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmitdetail',
            name='submit',
            field=models.ForeignKey(db_column=b'submit_id', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4', to='question.AssignmentSubmit'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='comment',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='level',
            field=models.SmallIntegerField(default=0, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='owner',
            field=models.ForeignKey(db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='parent',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='question.Charpter', null=True, verbose_name=b'\xe7\x88\xb6\xe7\xab\xa0\xe8\x8a\x82'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='path',
            field=models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='subject',
            field=models.ForeignKey(db_column=b'subject', verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', to='question.CodeSubject'),
        ),
        migrations.AlterField(
            model_name='charpter',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'\xe7\xab\xa0\xe8\x8a\x82'),
        ),
        migrations.AlterField(
            model_name='codeassignmentstatus',
            name='status_name',
            field=models.CharField(default=b'\xe8\x8d\x89\xe7\xa8\xbf', max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='codeassignmenttype',
            name='assignment_type_name',
            field=models.CharField(default=b'\xe6\x97\xa5\xe5\xb8\xb8\xe4\xbd\x9c\xe4\xb8\x9a', max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='codecontexttype',
            name='context_type_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='codequesthiontype',
            name='questhion_type_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='codesubject',
            name='subject_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', choices=[(b'\xe8\xaf\xad\xe6\x96\x87', b'\xe8\xaf\xad\xe6\x96\x87'), (b'\xe6\x95\xb0\xe5\xad\xa6', b'\xe6\x95\xb0\xe5\xad\xa6'), (b'\xe8\x8b\xb1\xe8\xaf\xad', b'\xe8\x8b\xb1\xe8\xaf\xad'), (b'\xe7\x89\xa9\xe7\x90\x86', b'\xe7\x89\xa9\xe7\x90\x86'), (b'\xe5\x8c\x96\xe5\xad\xa6', b'\xe5\x8c\x96\xe5\xad\xa6'), (b'\xe7\x94\x9f\xe7\x89\xa9', b'\xe7\x94\x9f\xe7\x89\xa9'), (b'\xe5\x8e\x86\xe5\x8f\xb2', b'\xe5\x8e\x86\xe5\x8f\xb2'), (b'\xe5\x9c\xb0\xe7\x90\x86', b'\xe5\x9c\xb0\xe7\x90\x86'), (b'\xe6\x94\xbf\xe6\xb2\xbb', b'\xe6\x94\xbf\xe6\xb2\xbb')]),
        ),
        migrations.AlterField(
            model_name='codesubmitstatus',
            name='submit_status_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'\xe6\x9c\xaa\xe5\x81\x9a', b'\xe6\x9c\xaa\xe5\x81\x9a'), (b'\xe5\xae\x8c\xe6\x88\x90', b'\xe5\xae\x8c\xe6\x88\x90'), (b'\xe8\x8d\x89\xe7\xa8\xbf', b'\xe8\x8d\x89\xe7\xa8\xbf'), (b'\xe8\xbf\x87\xe6\x9c\x9f', b'\xe8\xbf\x87\xe6\x9c\x9f')]),
        ),
        migrations.AlterField(
            model_name='knowegepoint',
            name='created_by',
            field=models.ForeignKey(related_name='created_knowege_points', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='knowegepoint',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='knowegepoint',
            name='owner',
            field=models.ForeignKey(related_name='own_knowege_points', db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='knowegepoint',
            name='ref_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xbc\x95\xe7\x94\xa8\xe6\xac\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='knowegepoint',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\x9f\xa5\xe8\xaf\x86\xe7\x82\xb9\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_name',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
        migrations.AlterField(
            model_name='library',
            name='owner',
            field=models.ForeignKey(db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='library',
            name='public',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x85\xac\xe5\xbc\x80'),
        ),
        migrations.AlterField(
            model_name='material',
            name='comments',
            field=models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_by',
            field=models.ForeignKey(related_name='created_materials', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='material',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='material',
            name='edit_by',
            field=models.ForeignKey(related_name='edited_materials', db_column=b'edit_by', verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='ref',
            field=models.ForeignKey(db_column=b'ref_id', blank=True, to='question.Material', null=True, verbose_name=b'\xe5\x8e\x9f\xe6\x9d\x90\xe6\x96\x99'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(default=b'', verbose_name=b'\xe5\x9b\x9e\xe7\xad\x94', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.ForeignKey(db_column=b'answer_type', verbose_name=b'\xe7\xad\x94\xe9\xa2\x98\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeContextType'),
        ),
        migrations.AlterField(
            model_name='question',
            name='charpter',
            field=models.ForeignKey(related_name='questions', db_column=b'charpter_id', verbose_name=b'\xe5\xbd\x92\xe5\xb1\x9e\xe7\xab\xa0\xe8\x8a\x82', to='question.Charpter'),
        ),
        migrations.AlterField(
            model_name='question',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(related_name='created_questions', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficultly',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe9\x9a\xbe\xe5\xba\xa6'),
        ),
        migrations.AlterField(
            model_name='question',
            name='edit_by',
            field=models.ForeignKey(related_name='edited_questions', db_column=b'edit_by', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe8\x80\x85'),
        ),
        migrations.AlterField(
            model_name='question',
            name='library',
            field=models.ForeignKey(db_column=b'library_id', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe9\xa6\x86', to='question.Library'),
        ),
        migrations.AlterField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(related_name='own_questions', db_column=b'owner', verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba', to='education.Org'),
        ),
        migrations.AlterField(
            model_name='question',
            name='ref',
            field=models.ForeignKey(related_name='distortion', db_column=b'ref_id', blank=True, to='question.Question', null=True, verbose_name=b'\xe5\x8e\x9f\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='question',
            name='share',
            field=models.NullBooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x88\x86\xe4\xba\xab'),
        ),
        migrations.AlterField(
            model_name='question',
            name='solve',
            field=models.TextField(default=b'', verbose_name=b'\xe8\xa7\xa3\xe6\x9e\x90', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.ForeignKey(related_name='questions', db_column=b'type', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeQuesthionType'),
        ),
        migrations.AlterField(
            model_name='questionknowlegepoint',
            name='index',
            field=models.ForeignKey(db_column=b'index', verbose_name=b'\xe7\x9f\xa5\xe8\xaf\x86\xe7\x82\xb9', to='question.KnowegePoint'),
        ),
        migrations.AlterField(
            model_name='questionknowlegepoint',
            name='questhion',
            field=models.ForeignKey(db_column=b'questhion_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question'),
        ),
        migrations.AlterField(
            model_name='questionsdyndifficulty',
            name='calc_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='questionsdyndifficulty',
            name='comments',
            field=models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='questionsdyndifficulty',
            name='diffcultty',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x9a\xbe\xe5\xba\xa6\xe7\xad\x89\xe7\xba\xa7'),
        ),
        migrations.AlterField(
            model_name='questionsdyndifficulty',
            name='question',
            field=models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question'),
        ),
        migrations.AlterField(
            model_name='weakpoint',
            name='question',
            field=models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question'),
        ),
        migrations.AlterField(
            model_name='weakpoint',
            name='user',
            field=models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f', to=settings.AUTH_USER_MODEL),
        ),
    ]
