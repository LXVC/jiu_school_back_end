# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0003_auto_20160722_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('created_by', models.ForeignKey(related_name='created_notices', db_column=b'create_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'notices',
            },
        ),
        migrations.CreateModel(
            name='NoticeTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notice', models.ForeignKey(to='education.Notice', db_column=b'notice_id')),
                ('org', models.ForeignKey(related_name='notices', db_column=b'org_id', to='education.Org', null=True)),
                ('user', models.ForeignKey(related_name='notices', db_column=b'user_id', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'notice_to',
            },
        ),
    ]
