# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devolucao', '0003_auto_20161005_0112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='quantidade_devolver',
            new_name='quantidade_total_a_devolver',
        ),
    ]
