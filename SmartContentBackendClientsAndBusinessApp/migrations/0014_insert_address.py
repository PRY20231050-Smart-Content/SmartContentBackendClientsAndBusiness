# Generated by Django 4.1.7 on 2023-07-23 23:50

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0013_alter_user_status'),
    ]

    operations = [
        migrations.RunSQL("""
          DROP PROCEDURE IF EXISTS insert_address;

          CREATE PROCEDURE insert_address(
            IN p_city VARCHAR(255),
            IN p_country VARCHAR(255),
            IN p_postal_code VARCHAR(50),
            IN p_street VARCHAR(255)
          )
          BEGIN
            INSERT INTO address(city, country, postal_code, street,created_at)
            VALUES (p_city, p_country, p_postal_code, p_street,now());
          END;
        """)
    ]
