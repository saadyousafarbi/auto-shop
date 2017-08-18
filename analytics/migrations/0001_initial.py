# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-17 04:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsRequestsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Record Date')),
                ('requests_counter_get', models.PositiveIntegerField(default=0, verbose_name=b'GET Requests Counter')),
                ('requests_counter_get_err', models.PositiveIntegerField(default=0, verbose_name=b'Failed GET Requests Counter')),
                ('requests_counter_post', models.PositiveIntegerField(default=0, verbose_name=b'POST Requests Counter')),
                ('requests_counter_post_err', models.PositiveIntegerField(default=0, verbose_name=b'Failed POST Requests Counter')),
            ],
        ),
    ]