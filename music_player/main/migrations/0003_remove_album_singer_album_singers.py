# Generated by Django 4.1.2 on 2022-10-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_song_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='singer',
        ),
        migrations.AddField(
            model_name='album',
            name='singers',
            field=models.ManyToManyField(to='main.singer'),
        ),
    ]
