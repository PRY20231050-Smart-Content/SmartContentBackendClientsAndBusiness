# Generated by Django 4.1.7 on 2023-07-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0019_remove_post_business_remove_posttracking_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
