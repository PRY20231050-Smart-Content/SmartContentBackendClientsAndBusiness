# Generated by Django 4.1.7 on 2023-07-23 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0010_get_all_industries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=50),
        ),
    ]
