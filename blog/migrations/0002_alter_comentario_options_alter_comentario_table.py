# Generated by Django 5.1.3 on 2024-12-02 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='comentario',
            table='comentarios',
        ),
    ]
