# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addNoms', '0004_auto_20161204_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('tm', models.DateTimeField(auto_now_add=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]