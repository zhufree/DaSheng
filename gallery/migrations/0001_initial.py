# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=5000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=3000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='user_messages', default=2, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField()),
                ('add_time', models.TimeField(auto_now=True)),
                ('is_show', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=20)),
                ('count', models.IntegerField(default=0)),
                ('is_author', models.BooleanField(default=False)),
                ('author_link', models.URLField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(related_name='has_photos', to='gallery.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ForeignKey(related_name='photo_comments', to='gallery.Photo'),
            preserve_default=True,
        ),
    ]
