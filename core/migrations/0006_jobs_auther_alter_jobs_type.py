# Generated by Django 4.2.5 on 2023-09-21 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_jobs_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='auther',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('by taske', 'by taske'), ('other', 'other'), ('full time', 'full time'), ('part time', 'part time')], default='full time', max_length=50),
        ),
    ]
