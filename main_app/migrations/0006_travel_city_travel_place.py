# Generated by Django 5.0 on 2023-12-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_travel_spots_finch_travel_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='city',
            field=models.CharField(default='Melbourne', max_length=20),
        ),
        migrations.AddField(
            model_name='travel',
            name='place',
            field=models.CharField(default='beach', max_length=20),
        ),
    ]
