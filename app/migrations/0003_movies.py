# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-18 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_credentialskey_moocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=345, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
    ]
