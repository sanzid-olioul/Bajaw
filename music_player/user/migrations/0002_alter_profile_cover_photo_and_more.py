# Generated by Django 4.1.2 on 2022-10-22 15:23

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.user_directory_path),
        ),
    ]
