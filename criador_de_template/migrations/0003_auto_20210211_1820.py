# Generated by Django 3.1.5 on 2021-02-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criador_de_template', '0002_auto_20210211_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='celular',
            field=models.CharField(default=9, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], default=5, max_length=11),
            preserve_default=False,
        ),
    ]
