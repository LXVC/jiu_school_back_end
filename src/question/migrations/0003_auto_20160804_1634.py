# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20160804_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesubject',
            name='subject_name',
            field=models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', choices=[('\u8bed\u6587', '\u8bed\u6587'), ('\u6570\u5b66', '\u6570\u5b66'), ('\u82f1\u8bed', '\u82f1\u8bed'), ('\u7269\u7406', '\u7269\u7406'), ('\u5316\u5b66', '\u5316\u5b66'), ('\u751f\u7269', '\u751f\u7269'), ('\u5386\u53f2', '\u5386\u53f2'), ('\u5730\u7406', '\u5730\u7406'), ('\u653f\u6cbb', '\u653f\u6cbb')]),
        ),
    ]
