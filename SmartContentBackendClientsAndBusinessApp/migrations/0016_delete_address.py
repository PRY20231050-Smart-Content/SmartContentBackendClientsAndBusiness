from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0015_update_address'),
    ]

    operations = [
        migrations.RunSQL("""
          DROP PROCEDURE IF EXISTS delete_address;

          CREATE PROCEDURE delete_address(IN p_id INT)
          BEGIN
            DELETE FROM address
            WHERE id = p_id;
          END;
        """)
    ]

