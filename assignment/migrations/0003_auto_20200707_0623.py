# Generated by Django 3.0.8 on 2020-07-07 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20200707_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='permanentAddress',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assignment.Address'),
        ),
    ]
