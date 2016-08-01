# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0011_keyteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade_name', models.CharField(default=b'\xe5\x88\x9d\xe4\xb8\x80', max_length=10, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7', blank=True)),
            ],
            options={
                'db_table': 'grades',
                'verbose_name': '\u5e74\u7ea7',
                'verbose_name_plural': '\u5e74\u7ea7',
            },
        ),
        migrations.AlterModelOptions(
            name='keyschool',
            options={'verbose_name': '\u540d\u724c\u5b66\u6821', 'verbose_name_plural': '\u540d\u724c\u5b66\u6821'},
        ),
        migrations.AddField(
            model_name='org',
            name='grade',
            field=models.ForeignKey(db_column=b'grade', blank=True, to='education.CodeGrade', null=True, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7'),
        ),
    ]
