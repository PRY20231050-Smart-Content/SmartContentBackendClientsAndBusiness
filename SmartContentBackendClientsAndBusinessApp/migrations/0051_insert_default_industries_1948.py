from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0034_servicebusiness_deleted_at'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO industries ( name, created_at) VALUES ('Construction Services', '2023-07-23 22:19:29');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries ( name, created_at) VALUES ('Cleaning Services',  '2023-07-23 23:04:45');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries ( name, created_at) VALUES ('Fields Services',  '2023-07-23 23:06:53');"
        ),
        migrations.RunSQL(
            "INSERT INTO industries ( name, created_at) VALUES ('Gourmet Services',  '2023-07-24 00:06:53');"
        ),
    ]
