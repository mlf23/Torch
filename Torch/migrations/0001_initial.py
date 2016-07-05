# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('giturl', models.URLField(max_length=1000)),
                ('gitFile', models.FileField(upload_to='Git/%Y/%m/%d')),
                ('newFile', models.FilePathField(recursive=True, path='Git/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='LoadFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to='file_load/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=250)),
                ('projects', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('language', models.ForeignKey(to='Torch.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('Lddfile', models.FileField(upload_to='Files/%Y/%m/%d')),
            ],
        ),
    ]
