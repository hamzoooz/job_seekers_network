# Generated by Django 4.2.5 on 2023-09-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_jobs_auther_alter_jobs_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='features',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('part time', 'part time'), ('full time', 'full time'), ('other', 'other'), ('by taske', 'by taske')], default='full time', max_length=50),
        ),
    ]