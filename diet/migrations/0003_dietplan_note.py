# Generated by Django 4.2.6 on 2023-11-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_alter_dietplan_diet_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='dietplan',
            name='note',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
