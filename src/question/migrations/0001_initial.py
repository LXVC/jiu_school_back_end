# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20160719_1440'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('questhion_num', models.IntegerField(default=2)),
                ('published_count', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'db_table': 'assignment',
            },
        ),
        migrations.CreateModel(
            name='AssignmentPublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share', models.NullBooleanField(default=False)),
                ('publish_date', models.DateTimeField(blank=True)),
                ('publish_date_start', models.DateTimeField(blank=True)),
                ('publish_date_end', models.DateTimeField(blank=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('assignment', models.ForeignKey(to='question.Assignment', db_column=b'assignment_id')),
                ('publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'publisher')),
                ('reciver_org', models.ForeignKey(to='education.Org', db_column=b'reciver_org')),
            ],
            options={
                'db_table': 'assignment_publish',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSubmit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.TextField()),
                ('start_date', models.DateTimeField(blank=True)),
                ('submit_date', models.DateTimeField(blank=True)),
                ('comment', models.CharField(max_length=500, blank=True)),
                ('assignment_publish', models.ForeignKey(to='question.AssignmentPublish', db_column=b'assignment_publish_id')),
            ],
            options={
                'db_table': 'assignment_submit',
            },
        ),
        migrations.CreateModel(
            name='AssignmentSubmitDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=500, blank=True)),
                ('checking_status', models.CharField(max_length=20, blank=True)),
                ('checking_context', models.CharField(max_length=500, blank=True)),
                ('checking_date', models.DateTimeField()),
                ('checking_comments', models.CharField(max_length=500, blank=True)),
                ('status', models.CharField(max_length=20, blank=True)),
                ('checking_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'checking_by')),
            ],
            options={
                'db_table': 'assignment_submit_detail',
            },
        ),
        migrations.CreateModel(
            name='Charpter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('path', models.CharField(max_length=200)),
                ('level', models.SmallIntegerField(default=0)),
                ('comment', models.CharField(max_length=500)),
                ('owner', models.ForeignKey(to='education.Org', db_column=b'owner')),
                ('parent', models.ForeignKey(db_column=b'parent_id', blank=True, to='question.Charpter', null=True)),
            ],
            options={
                'db_table': 'charpter',
            },
        ),
        migrations.CreateModel(
            name='CodeAssignmentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(default=b'\xe8\x8d\x89\xe7\xa8\xbf', max_length=20)),
            ],
            options={
                'db_table': 'code_assignment_status',
            },
        ),
        migrations.CreateModel(
            name='CodeAssignmentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_type_name', models.CharField(default=b'\xe6\x97\xa5\xe5\xb8\xb8\xe4\xbd\x9c\xe4\xb8\x9a', max_length=50)),
            ],
            options={
                'db_table': 'code_assignment_type',
            },
        ),
        migrations.CreateModel(
            name='CodeContextType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context_type_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_context_type',
            },
        ),
        migrations.CreateModel(
            name='CodeQuesthionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questhion_type_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'code_questhion_type',
            },
        ),
        migrations.CreateModel(
            name='CodeSubject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=20, choices=[(b'\xe8\xaf\xad\xe6\x96\x87', b'\xe8\xaf\xad\xe6\x96\x87'), (b'\xe6\x95\xb0\xe5\xad\xa6', b'\xe6\x95\xb0\xe5\xad\xa6'), (b'\xe8\x8b\xb1\xe8\xaf\xad', b'\xe8\x8b\xb1\xe8\xaf\xad'), (b'\xe7\x89\xa9\xe7\x90\x86', b'\xe7\x89\xa9\xe7\x90\x86'), (b'\xe5\x8c\x96\xe5\xad\xa6', b'\xe5\x8c\x96\xe5\xad\xa6'), (b'\xe7\x94\x9f\xe7\x89\xa9', b'\xe7\x94\x9f\xe7\x89\xa9'), (b'\xe5\x8e\x86\xe5\x8f\xb2', b'\xe5\x8e\x86\xe5\x8f\xb2'), (b'\xe5\x9c\xb0\xe7\x90\x86', b'\xe5\x9c\xb0\xe7\x90\x86'), (b'\xe6\x94\xbf\xe6\xb2\xbb', b'\xe6\x94\xbf\xe6\xb2\xbb')])),
            ],
            options={
                'db_table': 'code_subject',
            },
        ),
        migrations.CreateModel(
            name='CodeSubmitStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submit_status_name', models.CharField(max_length=20, choices=[(b'\xe6\x9c\xaa\xe5\x81\x9a', b'\xe6\x9c\xaa\xe5\x81\x9a'), (b'\xe5\xae\x8c\xe6\x88\x90', b'\xe5\xae\x8c\xe6\x88\x90'), (b'\xe8\x8d\x89\xe7\xa8\xbf', b'\xe8\x8d\x89\xe7\xa8\xbf'), (b'\xe8\xbf\x87\xe6\x9c\x9f', b'\xe8\xbf\x87\xe6\x9c\x9f')])),
            ],
            options={
                'db_table': 'code_submit_status',
            },
        ),
        migrations.CreateModel(
            name='KnowegePoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('ref_count', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(related_name='created_knowege_points', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='own_knowege_points', db_column=b'owner', to='education.Org')),
            ],
            options={
                'db_table': 'knowege_point',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('library_name', models.CharField(max_length=100)),
                ('public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to='education.Org', db_column=b'owner')),
            ],
            options={
                'db_table': 'library',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(related_name='created_materials', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_materials', db_column=b'edit_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('ref', models.ForeignKey(db_column=b'ref_id', to='question.Material', null=True)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('answer', models.TextField()),
                ('difficultly', models.SmallIntegerField(default=1)),
                ('solve', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('share', models.NullBooleanField()),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('answer_type', models.ForeignKey(to='question.CodeContextType', db_column=b'answer_type')),
                ('charpter', models.ForeignKey(related_name='questions', db_column=b'charpter_id', to='question.Charpter')),
                ('created_by', models.ForeignKey(related_name='created_questions', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_questions', db_column=b'edit_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('library', models.ForeignKey(to='question.Library', db_column=b'library_id')),
                ('owner', models.ForeignKey(related_name='own_questions', db_column=b'owner', to='education.Org')),
                ('ref', models.ForeignKey(related_name='distortion', db_column=b'ref_id', to='question.Question', null=True)),
                ('type', models.ForeignKey(related_name='questions', db_column=b'type', to='question.CodeQuesthionType')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionKnowlegePoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.ForeignKey(to='question.KnowegePoint', db_column=b'index')),
                ('questhion', models.ForeignKey(to='question.Question', db_column=b'questhion_id')),
            ],
            options={
                'db_table': 'question_knowlege_point',
            },
        ),
        migrations.CreateModel(
            name='QuestionsDyndifficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diffcultty', models.IntegerField(default=0)),
                ('calc_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('question', models.ForeignKey(to='question.Question', db_column=b'question_id')),
            ],
            options={
                'db_table': 'questions_dyndifficulty',
            },
        ),
        migrations.CreateModel(
            name='WeakPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(to='question.Question', db_column=b'question_id')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'user_id')),
            ],
            options={
                'db_table': 'weak_point',
            },
        ),
        migrations.AddField(
            model_name='charpter',
            name='subject',
            field=models.ForeignKey(to='question.CodeSubject', db_column=b'subject'),
        ),
        migrations.AddField(
            model_name='assignmentsubmitdetail',
            name='question',
            field=models.ForeignKey(to='question.Question', db_column=b'question_id'),
        ),
        migrations.AddField(
            model_name='assignmentsubmitdetail',
            name='submit',
            field=models.ForeignKey(to='question.AssignmentSubmit', db_column=b'submit_id'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='status',
            field=models.ForeignKey(to='question.CodeSubmitStatus', db_column=b'status'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='submiter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'submiter'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='charpter',
            field=models.ForeignKey(related_name='assignments', db_column=b'charpter_id', to='question.Charpter'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='created_by',
            field=models.ForeignKey(related_name='created_assignment', db_column=b'created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='owner',
            field=models.ForeignKey(related_name='own_assignments', db_column=b'owner', to='education.Org'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='status',
            field=models.ForeignKey(to='question.CodeAssignmentStatus', db_column=b'status'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='type',
            field=models.ForeignKey(to='question.CodeAssignmentType', db_column=b'type'),
        ),
    ]
