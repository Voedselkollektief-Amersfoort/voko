# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_userprofile_share_contact_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='share_contact_info',
        ),
    ]
