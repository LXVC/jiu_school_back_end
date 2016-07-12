# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_remove_profile_md5passwdstr'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='md5passwdstr',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
