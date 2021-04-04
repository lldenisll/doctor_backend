# Generated by Django 3.1.7 on 2021-04-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0005_auto_20210403_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_estudo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='espacamento_slice',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_acesso',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paciente_id',
            field=models.TextField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='paciente_sexo',
            field=models.TextField(blank=True),
        ),
    ]
