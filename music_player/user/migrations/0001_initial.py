# Generated by Django 4.1.2 on 2022-10-22 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cover_photo', models.ImageField(upload_to=user.models.user_directory_path)),
                ('profile_photo', models.ImageField(upload_to=user.models.user_directory_path)),
                ('user_type', models.CharField(choices=[('Pri', 'Premium'), ('Reg', 'Regular')], default='Reg', max_length=4)),
                ('liked_song', models.ManyToManyField(blank=True, null=True, to='main.songs')),
            ],
        ),
    ]
