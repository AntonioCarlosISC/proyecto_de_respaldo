# Generated by Django 5.0.2 on 2024-02-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_usuariopersonalizado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('investigador', models.CharField(max_length=100, verbose_name='Nombre del investigador que subio el archivo')),
                ('estadoCalificacion', models.CharField(blank=True, max_length=20, verbose_name='Estado de la calificacion')),
                ('calificacion', models.IntegerField(max_length=3, verbose_name='Calificacion del trabajo')),
                ('ultimaRevision', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
