# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('questhion_num', models.IntegerField(default=2, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe6\x95\xb0\xe9\x87\x8f')),
                ('published_count', models.IntegerField(default=0, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x95\xb0')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'db_table': 'assignment',
                'verbose_name': '\u4f5c\u4e1a',
                'verbose_name_plural': '\u4f5c\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='AssignmentPublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share', models.NullBooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x88\x86\xe4\xba\xab')),
                ('publish_date', models.DateTimeField(verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('publish_date_start', models.DateTimeField(verbose_name=b'\xe6\x9c\x80\xe6\x97\xa9\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('publish_date_end', models.DateTimeField(verbose_name=b'\xe6\x9c\x80\xe6\x99\x9a\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('assignment', models.ForeignKey(db_column=b'assignment_id', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a', to='question.Assignment')),
                ('publisher', models.ForeignKey(db_column=b'publisher', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
                ('reciver_org', models.ForeignKey(db_column=b'reciver_org', verbose_name=b'\xe6\x8e\xa5\xe6\x94\xb6\xe7\xbb\x84\xe7\xbb\x87', to='education.Org')),
            ],
            options={
                'db_table': 'assignment_publish',
                'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u60c5\u51b5',
                'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u60c5\u51b5',
            },
        ),
        migrations.CreateModel(
            name='AssignmentQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField()),
                ('extra', models.CharField(default=b'', max_length=500, blank=True)),
                ('assignment', models.ForeignKey(to='question.Assignment', db_column=b'assignment_id')),
            ],
            options={
                'db_table': 'assignment_questions',
                'verbose_name': '\u4f5c\u4e1a\u4e0e\u9898\u76ee',
                'verbose_name_plural': '\u4f5c\u4e1a\u4e0e\u9898\u76ee',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('start_date', models.DateTimeField(verbose_name=b'\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('submit_date', models.DateTimeField(verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('comment', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('assignment_publish', models.ForeignKey(db_column=b'assignment_publish_id', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x8f\x90\xe4\xba\xa4', to='question.AssignmentPublish')),
            ],
            options={
                'db_table': 'assignment_submit',
                'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001',
                'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSubmitDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=500, verbose_name=b'\xe7\xad\x94\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('checking_status', models.CharField(max_length=20, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('checking_context', models.CharField(max_length=500, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('checking_date', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('checking_comments', models.CharField(max_length=500, verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('status', models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
                ('checking_by', models.ForeignKey(db_column=b'checking_by', verbose_name=b'\xe6\x89\xb9\xe6\x94\xb9\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'assignment_submit_detail',
                'verbose_name': '\u4f5c\u4e1a\u8be6\u60c5',
                'verbose_name_plural': '\u4f5c\u4e1a\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Charpter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xe7\xab\xa0\xe8\x8a\x82')),
                ('path', models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae')),
                ('level', models.SmallIntegerField(default=0, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab')),
                ('comment', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('owner', models.ForeignKey(db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', db_column=b'parent_id', blank=True, to='question.Charpter', null=True, verbose_name=b'\xe7\x88\xb6\xe7\xab\xa0\xe8\x8a\x82')),
            ],
            options={
                'db_table': 'charpter',
                'verbose_name': '\u7ae0\u8282',
                'verbose_name_plural': '\u7ae0\u8282',
            },
        ),
        migrations.CreateModel(
            name='CodeAssignmentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(default=b'\xe8\x8d\x89\xe7\xa8\xbf', max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            options={
                'db_table': 'code_assignment_status',
                'verbose_name': '\u4f5c\u4e1a\u72b6\u6001',
                'verbose_name_plural': '\u4f5c\u4e1a\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='CodeAssignmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_type_name', models.CharField(default=b'\xe6\x97\xa5\xe5\xb8\xb8\xe4\xbd\x9c\xe4\xb8\x9a', max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'db_table': 'code_assignment_type',
                'verbose_name': '\u4f5c\u4e1a\u7c7b\u578b',
                'verbose_name_plural': '\u4f5c\u4e1a\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='CodeContextType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context_type_name', models.CharField(max_length=20, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u6587\u5b57', '\u6587\u5b57'), ('\u56fe\u7247', '\u56fe\u7247')])),
            ],
            options={
                'db_table': 'code_context_type',
                'verbose_name': '\u7b54\u6848\u7c7b\u578b',
                'verbose_name_plural': '\u7b54\u6848\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='CodeQuesthionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questhion_type_name', models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u4e3b\u89c2\u9898', '\u4e3b\u89c2\u9898'), ('\u5ba2\u89c2\u9898', '\u5ba2\u89c2\u9898')])),
            ],
            options={
                'db_table': 'code_questhion_type',
                'verbose_name': '\u9898\u76ee\u7c7b\u578b',
                'verbose_name_plural': '\u9898\u76ee\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='CodeSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', choices=[('\u8bed\u6587', '\u8bed\u6587'), ('\u6570\u5b66', '\u6570\u5b66'), ('\u82f1\u8bed', '\u82f1\u8bed'), ('\u7269\u7406', '\u7269\u7406'), ('\u5316\u5b66', '\u5316\u5b66'), ('\u751f\u7269', '\u751f\u7269'), ('\u5386\u53f2', '\u5386\u53f2'), ('\u5730\u7406', '\u5730\u7406'), ('\u653f\u6cbb', '\u653f\u6cbb')])),
            ],
            options={
                'db_table': 'code_subject',
                'verbose_name': '\u79d1\u76ee',
                'verbose_name_plural': '\u79d1\u76ee',
            },
        ),
        migrations.CreateModel(
            name='CodeSubmitStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_status_name', models.CharField(max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'\xe6\x9c\xaa\xe5\x81\x9a', b'\xe6\x9c\xaa\xe5\x81\x9a'), (b'\xe5\xae\x8c\xe6\x88\x90', b'\xe5\xae\x8c\xe6\x88\x90'), (b'\xe8\x8d\x89\xe7\xa8\xbf', b'\xe8\x8d\x89\xe7\xa8\xbf'), (b'\xe8\xbf\x87\xe6\x9c\x9f', b'\xe8\xbf\x87\xe6\x9c\x9f')])),
            ],
            options={
                'db_table': 'code_submit_status',
                'verbose_name': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001',
                'verbose_name_plural': '\u4f5c\u4e1a\u63d0\u4ea4\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='KnowegePoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe7\x9f\xa5\xe8\xaf\x86\xe7\x82\xb9\xe5\x90\x8d\xe5\xad\x97')),
                ('ref_count', models.IntegerField(default=0, verbose_name=b'\xe5\xbc\x95\xe7\x94\xa8\xe6\xac\xa1\xe6\x95\xb0')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('created_by', models.ForeignKey(related_name='created_knowege_points', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='own_knowege_points', db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', db_column=b'parent_id', blank=True, to='question.KnowegePoint', null=True, verbose_name=b'\xe7\x88\xb6\xe7\x9f\xa5\xe8\xaf\x86\xe7\x82\xb9')),
            ],
            options={
                'db_table': 'knowege_point',
                'verbose_name': '\u77e5\u8bc6\u70b9',
                'verbose_name_plural': '\u77e5\u8bc6\u70b9',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('library_name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('public', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x85\xac\xe5\xbc\x80')),
                ('owner', models.ForeignKey(db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org')),
            ],
            options={
                'db_table': 'library',
                'verbose_name': '\u56fe\u4e66\u9986',
                'verbose_name_plural': '\u56fe\u4e66\u9986',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('content', models.TextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('comments', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_materials', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_materials', db_column=b'edit_by', verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe8\x80\x85', to=settings.AUTH_USER_MODEL, null=True)),
                ('ref', models.ForeignKey(db_column=b'ref_id', blank=True, to='question.Material', null=True, verbose_name=b'\xe5\x8e\x9f\xe6\x9d\x90\xe6\x96\x99')),
            ],
            options={
                'db_table': 'materials',
                'verbose_name': '\u6750\u6599',
                'verbose_name_plural': '\u6750\u6599',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe5\x86\x85\xe5\xae\xb9')),
                ('answer', models.TextField(default=b'', verbose_name=b'\xe5\x9b\x9e\xe7\xad\x94', blank=True)),
                ('difficultly', models.SmallIntegerField(default=1, verbose_name=b'\xe9\x9a\xbe\xe5\xba\xa6')),
                ('solve', models.TextField(default=b'', verbose_name=b'\xe8\xa7\xa3\xe6\x9e\x90', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('share', models.NullBooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x88\x86\xe4\xba\xab')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('answer_type', models.ForeignKey(db_column=b'answer_type', verbose_name=b'\xe7\xad\x94\xe9\xa2\x98\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeContextType')),
                ('charpter', models.ForeignKey(related_name='questions', db_column=b'charpter_id', verbose_name=b'\xe5\xbd\x92\xe5\xb1\x9e\xe7\xab\xa0\xe8\x8a\x82', to='question.Charpter')),
                ('created_by', models.ForeignKey(related_name='created_questions', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_questions', db_column=b'edit_by', blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xe7\xbc\x96\xe8\xbe\x91\xe8\x80\x85')),
                ('library', models.ForeignKey(db_column=b'library_id', verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe9\xa6\x86', to='question.Library')),
                ('owner', models.ForeignKey(related_name='own_questions', db_column=b'owner', verbose_name=b'\xe6\x89\x80\xe6\x9c\x89\xe4\xba\xba', to='education.Org')),
                ('ref', models.ForeignKey(related_name='distortion', db_column=b'ref_id', blank=True, to='question.Question', null=True, verbose_name=b'\xe5\x8e\x9f\xe9\xa2\x98')),
                ('type', models.ForeignKey(related_name='questions', db_column=b'type', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeQuesthionType')),
            ],
            options={
                'db_table': 'questions',
                'verbose_name': '\u9898\u76ee',
                'verbose_name_plural': '\u9898\u76ee',
            },
        ),
        migrations.CreateModel(
            name='QuestionKnowlegePoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.ForeignKey(db_column=b'index', verbose_name=b'\xe7\x9f\xa5\xe8\xaf\x86\xe7\x82\xb9', to='question.KnowegePoint')),
                ('questhion', models.ForeignKey(db_column=b'questhion_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question')),
            ],
            options={
                'db_table': 'question_knowlege_point',
                'verbose_name': '\u9898\u76ee\u548c\u77e5\u8bc6\u70b9\u5bf9\u5e94\u5173\u7cfb',
                'verbose_name_plural': '\u9898\u76ee\u548c\u77e5\u8bc6\u70b9\u5bf9\u5e94\u5173\u7cfb',
            },
        ),
        migrations.CreateModel(
            name='QuestionsDyndifficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diffcultty', models.IntegerField(default=0, verbose_name=b'\xe9\x9a\xbe\xe5\xba\xa6\xe7\xad\x89\xe7\xba\xa7')),
                ('calc_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('comments', models.CharField(max_length=500, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('question', models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question')),
            ],
            options={
                'db_table': 'questions_dyndifficulty',
                'verbose_name': '\u9898\u76ee\u96be\u5ea6',
                'verbose_name_plural': '\u9898\u76ee\u96be\u5ea6',
            },
        ),
        migrations.CreateModel(
            name='WeakPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae', to='question.Question')),
                ('user', models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'weak_point',
                'verbose_name': '\u5b66\u751f\u7684\u8584\u5f31\u77e5\u8bc6',
                'verbose_name_plural': '\u5b66\u751f\u7684\u8584\u5f31\u77e5\u8bc6',
            },
        ),
        migrations.AddField(
            model_name='charpter',
            name='subject',
            field=models.ForeignKey(db_column=b'subject', verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', to='question.CodeSubject'),
        ),
        migrations.AddField(
            model_name='assignmentsubmitdetail',
            name='question',
            field=models.ForeignKey(db_column=b'question_id', verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', to='question.Question'),
        ),
        migrations.AddField(
            model_name='assignmentsubmitdetail',
            name='submit',
            field=models.ForeignKey(db_column=b'submit_id', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4', to='question.AssignmentSubmit'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe7\x8a\xb6\xe6\x80\x81', to='question.CodeSubmitStatus'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='submiter',
            field=models.ForeignKey(db_column=b'submiter', verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe4\xba\xba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignmentquestions',
            name='question',
            field=models.ForeignKey(to='question.Question', db_column=b'question_id'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='charpter',
            field=models.ForeignKey(related_name='assignments', db_column=b'charpter_id', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe7\xab\xa0\xe8\x8a\x82', to='question.Charpter'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='created_by',
            field=models.ForeignKey(related_name='created_assignment', db_column=b'created_by', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='owner',
            field=models.ForeignKey(related_name='own_assignments', db_column=b'owner', verbose_name=b'\xe6\x8b\xa5\xe6\x9c\x89\xe8\x80\x85', to='education.Org'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.ForeignKey(db_column=b'status', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', to='question.CodeAssignmentStatus'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='type',
            field=models.ForeignKey(db_column=b'type', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', to='question.CodeAssignmentType'),
        ),
    ]
