# Generated by Django 4.1.7 on 2023-08-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0033_remove_servicebusiness_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebusiness',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
