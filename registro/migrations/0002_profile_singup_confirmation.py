# Generated by Django 3.1.5 on 2021-01-25 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='singup_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]
