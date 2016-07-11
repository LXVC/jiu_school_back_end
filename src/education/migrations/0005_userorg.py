# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_auto_20160711_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.ForeignKey(to='education.Org', db_column=b'org_id')),
                ('user', models.ForeignKey(to='education.User', db_column=b'user_id')),
            ],
            options={
                'db_table': 'user_org',
            },
        ),
    ]
