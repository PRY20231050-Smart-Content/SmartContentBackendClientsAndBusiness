from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0014_insert_address'),
    ]

    operations = [
        migrations.RunSQL("""
          DROP PROCEDURE IF EXISTS update_address;

          CREATE PROCEDURE update_address(
            IN p_id INT,
            IN p_city VARCHAR(255),
            IN p_country VARCHAR(255),
            IN p_postal_code VARCHAR(50),
            IN p_street VARCHAR(255)
          )
          BEGIN
            UPDATE address
            SET city = p_city,
                country = p_country,
                postal_code = p_postal_code,
                street = p_street
            WHERE id = p_id;
          END;
        """)
    ]

