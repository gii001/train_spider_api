# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EasyName', models.CharField(max_length=b'20')),
                ('RealName', models.CharField(max_length=b'20')),
                ('StartStation', models.CharField(max_length=b'10')),
                ('StopSttation', models.CharField(max_length=b'10')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NowNum', models.IntegerField(max_length=b'10')),
                ('NowStation', models.CharField(max_length=b'10')),
                ('EasyName', models.ForeignKey(to='train.Basic_info')),
            ],
        ),
    ]
