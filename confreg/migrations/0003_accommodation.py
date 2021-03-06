# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('confreg', '0002_person_conference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=30)),
                ('capacity', models.IntegerField()),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confreg.Conference')),
            ],
        ),
    ]
