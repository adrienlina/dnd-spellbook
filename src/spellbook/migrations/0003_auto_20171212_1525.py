# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0002_spellbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpellUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prepared', models.BooleanField(default=False)),
                ('spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook.Spell')),
                ('spellbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spellbook.Spellbook')),
            ],
        ),
        migrations.AddField(
            model_name='spellbook',
            name='spells',
            field=models.ManyToManyField(through='spellbook.SpellUsage', to='spellbook.Spell'),
        ),
        migrations.AlterUniqueTogether(
            name='spellusage',
            unique_together=set([('spell', 'spellbook')]),
        ),
    ]
