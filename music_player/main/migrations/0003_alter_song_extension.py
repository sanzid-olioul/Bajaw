# Generated by Django 4.1.2 on 2022-10-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_songs_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='extension',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
    ]
