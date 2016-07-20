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
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(related_name='created_materials', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_materials', db_column=b'edit_by', to=settings.AUTH_USER_MODEL, null=True)),
                ('ref', models.ForeignKey(db_column=b'ref_id', blank=True, to='question.Material', null=True)),
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
                ('kp', models.TextField()),
                ('solve', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('share', models.NullBooleanField()),
                ('comments', models.CharField(max_length=500, blank=True)),
                ('answer_type', models.ForeignKey(to='question.CodeContextType', db_column=b'answer_type')),
                ('charpter', models.ForeignKey(to='question.Charpter', db_column=b'charpter_id')),
                ('created_by', models.ForeignKey(related_name='created_questions', db_column=b'created_by', to=settings.AUTH_USER_MODEL)),
                ('edit_by', models.ForeignKey(related_name='edited_questions', db_column=b'edit_by', to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(to='question.Library', db_column=b'library_id')),
                ('owner', models.ForeignKey(related_name='questions', db_column=b'owner', to=settings.AUTH_USER_MODEL)),
                ('ref', models.ForeignKey(db_column=b'ref_id', blank=True, to='question.Question', null=True)),
                ('type', models.ForeignKey(to='question.CodeQuesthionType', db_column=b'type')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.AddField(
            model_name='charpter',
            name='subject',
            field=models.ForeignKey(to='question.CodeSubject', db_column=b'subject'),
        ),
    ]
