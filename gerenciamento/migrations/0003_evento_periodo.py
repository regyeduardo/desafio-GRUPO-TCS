# Generated by Django 4.0.1 on 2022-01-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0002_rename_codigo_status_maquina_status_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='periodo',
            field=models.IntegerField(null=True),
        ),
    ]
