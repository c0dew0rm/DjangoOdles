# Generated by Django 3.0.8 on 2020-07-07 07:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_profile_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
