# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_tag_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(related_name='user_messages', default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
