# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-27 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_languages_linklanguages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ebooks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Linkebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namelink', models.CharField(blank=True, max_length=245, null=True)),
                ('url', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'linkebooks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Textbooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=245, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=445, null=True)),
            ],
            options={
                'db_table': 'textbooks',
                'managed': False,
            },
        ),
    ]