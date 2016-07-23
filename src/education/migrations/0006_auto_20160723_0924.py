# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_auto_20160723_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeto',
            name='org',
            field=models.ForeignKey(related_name='notices', db_column=b'org_id', blank=True, to='education.Org', null=True),
        ),
        migrations.AlterField(
            model_name='noticeto',
            name='user',
            field=models.ForeignKey(related_name='notices', db_column=b'user_id', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
