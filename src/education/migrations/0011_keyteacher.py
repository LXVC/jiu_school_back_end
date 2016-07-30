# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0010_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(default=10, verbose_name=b'\xe7\xad\x89\xe7\xba\xa7', blank=True)),
                ('details', models.CharField(default=b'', max_length=20, blank=True)),
                ('teacher', models.ForeignKey(db_column=b'user_id', verbose_name=b'\xe6\x95\x99\xe5\xb8\x88', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'keyteacher',
                'verbose_name': '\u540d\u724c\u6559\u5e08',
                'verbose_name_plural': '\u540d\u724c\u6559\u5e08',
            },
        ),
    ]
