# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeOrgType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_type_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='userorg',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='org',
            name='type',
            field=models.ForeignKey(db_column=b'type', verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe7\xb1\xbb\xe5\x9e\x8b', to='education.CodeOrgType'),
        ),
    ]
