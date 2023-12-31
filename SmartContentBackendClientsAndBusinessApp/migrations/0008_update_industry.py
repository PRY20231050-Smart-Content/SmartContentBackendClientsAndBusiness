# Generated by Django 4.1.7 on 2023-07-23 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0007_insert_industry'),
    ]

    operations = [
        migrations.RunSQL("""

          DROP PROCEDURE IF EXISTS update_industry;

          CREATE PROCEDURE update_industry(IN p_id INT, IN p_name VARCHAR(360))
          BEGIN
          
          UPDATE industries
          SET name = p_name
          WHERE id = p_id;
          END 
        """)
    ]
