# Generated by Django 4.2.5 on 2023-09-21 11:29

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='categoies/image')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile/profiles')),
                ('cover', models.ImageField(upload_to='profile/covers')),
                ('location', models.URLField()),
                ('campany', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descriptiion', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='post/images')),
                ('tags', models.CharField(max_length=15)),
                ('craet_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('number_of_like', models.IntegerField(default=0)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comments')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=5000)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('cite', models.CharField(blank=True, max_length=15, null=True)),
                ('image', models.FileField(default='img\\post.png', upload_to='jobs/image')),
                ('content', ckeditor.fields.RichTextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('trend', models.BooleanField(default=True)),
                ('approve', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
                ('applyed', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('full time', 'full time'), ('other', 'other'), ('by taske', 'by taske'), ('part time', 'part time')], default='fulltime', max_length=50)),
                ('time', models.CharField(choices=[('on site', 'on site'), ('remotly ', 'remotly '), ('other', 'other')], default='on site', max_length=50)),
                ('slary', models.IntegerField(blank=True, null=True)),
                ('location', models.URLField(blank=True, default='world', null=True)),
                ('tage', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_view', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('auther', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.category')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
