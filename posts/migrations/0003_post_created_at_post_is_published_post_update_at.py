# Generated by Django 4.2.18 on 2025-01-22 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options_post_likes_post_title_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 1, 22, 11, 3, 36, 32196)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
