# Generated by Django 4.2.5 on 2023-09-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_fitures_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
