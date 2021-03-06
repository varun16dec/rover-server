# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitutde', models.FloatField()),
                ('accuracy', models.IntegerField()),
                ('dateTime', models.DateTimeField()),
            ],
            options={
                'ordering': ('dateTime',),
            },
        ),
    ]
