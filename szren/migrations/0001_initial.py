# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-09-07 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=520, null=True, verbose_name='题目')),
                ('options', models.TextField(blank=True, null=True, verbose_name='选项')),
                ('result', models.CharField(blank=True, max_length=13, null=True, verbose_name='答案')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('number', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'verbose_name_plural': '专业信息',
                'verbose_name': '专业信息',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('number', models.CharField(blank=True, max_length=12, null=True)),
                ('pro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sz_pro', to='szren.Professional', verbose_name='所属专业')),
            ],
            options={
                'verbose_name_plural': '科目信息',
                'verbose_name': '科目信息',
            },
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='pro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mu_pro', to='szren.Professional', verbose_name='所属专业'),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mu_sub', to='szren.Subjects', verbose_name='所属科目'),
        ),
    ]
