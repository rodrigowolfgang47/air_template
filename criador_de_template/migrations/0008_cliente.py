# Generated by Django 3.1.5 on 2021-02-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criador_de_template', '0007_auto_20210203_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
