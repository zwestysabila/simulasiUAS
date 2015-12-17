# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20150922_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='statusnya',
        ),
        migrations.AddField(
            model_name='item',
            name='angka',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='angkaacak',
            field=models.IntegerField(default=0),
        ),
    ]
