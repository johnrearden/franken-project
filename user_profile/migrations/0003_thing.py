# Generated by Django 4.2.6 on 2023-12-23 16:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_video_clip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('array', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
    ]
