# Generated by Django 4.1.7 on 2023-02-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
