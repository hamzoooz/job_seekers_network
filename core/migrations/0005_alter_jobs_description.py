# Generated by Django 4.2.5 on 2023-09-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_jobs_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
