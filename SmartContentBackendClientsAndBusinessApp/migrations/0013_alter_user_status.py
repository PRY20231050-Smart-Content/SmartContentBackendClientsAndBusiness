# Generated by Django 4.1.7 on 2023-07-23 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0012_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], max_length=50, null=True),
        ),
    ]