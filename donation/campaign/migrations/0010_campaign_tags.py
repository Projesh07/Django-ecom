# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0009_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=models.ManyToManyField(to='campaign.Tag'),
        ),
    ]
