# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0003_auto_20171212_1242'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spellusage',
            unique_together=set([('spell', 'spellbook')]),
        ),
    ]
