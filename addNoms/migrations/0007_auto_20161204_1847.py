# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addNoms', '0006_auto_20161204_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergoal',
            name='pw',
        ),
        migrations.AddField(
            model_name='journalentry',
            name='foodID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='addNoms.Food'),
            preserve_default=False,
        ),
    ]