# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_auto_20150716_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=3000)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='user_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(related_name='has_photos', to='gallery.Tag', blank=True),
            preserve_default=True,
        ),
    ]
