# Generated by Django 5.0 on 2023-12-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_cat_feeding_finch_alter_feeding_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='finch',
            name='travel_spots',
            field=models.ManyToManyField(to='main_app.travel'),
        ),
    ]
