# Generated by Django 4.1.7 on 2023-08-26 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0028_rename_experience_years_business_facebook_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='values',
            new_name='logo_carpet',
        ),
    ]
