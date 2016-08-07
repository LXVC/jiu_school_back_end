# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20160804_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField()),
                ('extra', models.CharField(default=b'', max_length=500, blank=True)),
            ],
            options={
                'db_table': 'assignment_questions',
                'verbose_name': '\u4f5c\u4e1a\u4e0e\u9898\u76ee',
                'verbose_name_plural': '\u4f5c\u4e1a\u4e0e\u9898\u76ee',
            },
        ),
        migrations.AddField(
            model_name='knowegepoint',
            name='level',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='knowegepoint',
            name='parent',
            field=models.ForeignKey(db_column=b'parent_id', blank=True, to='question.KnowegePoint', null=True),
        ),
        migrations.AddField(
            model_name='knowegepoint',
            name='path',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='published_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='codecontexttype',
            name='context_type_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u6587\u5b57', '\u6587\u5b57'), ('\u56fe\u7247', '\u56fe\u7247')]),
        ),
        migrations.AlterField(
            model_name='codequesthiontype',
            name='questhion_type_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u4e3b\u89c2\u9898', '\u4e3b\u89c2\u9898'), ('\u5ba2\u89c2\u9898', '\u5ba2\u89c2\u9898')]),
        ),
        migrations.AddField(
            model_name='assignmentquestions',
            name='assignment',
            field=models.ForeignKey(to='question.Assignment', db_column=b'assignment_id'),
        ),
        migrations.AddField(
            model_name='assignmentquestions',
            name='question',
            field=models.ForeignKey(to='question.Question', db_column=b'question_id'),
        ),
    ]
