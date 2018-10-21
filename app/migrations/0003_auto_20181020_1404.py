# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-20 14:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181020_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_email_address',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='neighbourhood_id',
            new_name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='project',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Comments'),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Location'),
        ),
        migrations.AddField(
            model_name='project',
            name='postDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Review'),
        ),
    ]