# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20160719_1440'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('questhion_num', models.IntegerField(default=2)),
                ('charpter', models.IntegerField(default=1)),
                ('owner', models.IntegerField(default=1)),
                ('published_count', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_assignment', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
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
                ('assignment_publish', models.ForeignKey(to='question.AssignmentPublish', db_column=b'assignment_publish')),
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
                ('question', models.ForeignKey(to='question.Question', db_column=b'question_id')),
                ('submit', models.ForeignKey(to='question.AssignmentSubmit', db_column=b'submit_id')),
            ],
            options={
                'db_table': 'assignment_submit_detail',
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
                ('assignment_type_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'code_assignment_type',
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
                ('idx', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('ref_count', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'created_by')),
                ('owner', models.ForeignKey(related_name='knowege_points', db_column=b'owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'knowege_point',
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
            name='status',
            field=models.ForeignKey(to='question.CodeAssignmentStatus', db_column=b'status'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='type',
            field=models.ForeignKey(to='question.CodeAssignmentType', db_column=b'type'),
        ),
    ]
