# Generated by Django 3.1.5 on 2021-02-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criador_de_template', '0004_auto_20210212_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.BooleanField(default=False),
        ),
    ]
