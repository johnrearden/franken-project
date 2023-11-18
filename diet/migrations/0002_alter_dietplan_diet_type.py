# Generated by Django 4.2.6 on 2023-11-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='diet_type',
            field=models.CharField(choices=[('VG', 'Vegetarian'), ('VN', 'Vegan'), ('MT', 'Meat'), ('PS', 'Pescatarian')], default=1, max_length=2),
        ),
    ]
