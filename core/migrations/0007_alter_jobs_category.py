# Generated by Django 4.2.5 on 2023-09-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category'),
        ),
    ]
