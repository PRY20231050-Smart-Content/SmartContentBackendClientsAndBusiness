from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0045_update_business'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO industries (id, name, created_at) VALUES (1, 'Construction Services', '2023-07-23 22:19:29');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries (id, name, created_at) VALUES (2, 'Cleaning Services',  '2023-07-23 23:04:45');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries (id, name, created_at) VALUES (3, 'Fields Services',  '2023-07-23 23:06:53');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries (id, name, created_at) VALUES (4, 'Gourmet Services',  '2023-07-24 00:06:53');"
        ),
    ]