# Generated by Django 4.1.2 on 2022-10-23 17:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='liked_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
