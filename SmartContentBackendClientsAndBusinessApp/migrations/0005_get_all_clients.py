# Generated by Django 4.1.7 on 2023-07-23 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartContentBackendClientsAndBusinessApp', '0004_delete_client'),
    ]

    operations = [
        migrations.RunSQL("""
            DROP PROCEDURE IF EXISTS sp_get_clients;

            CREATE PROCEDURE sp_get_clients(
            IN _text VARCHAR(250),
            IN date_from DATE,
            IN date_to DATE,
            IN perpage INT,
            IN npage INT,
            IN order_by VARCHAR(255),
            IN orden VARCHAR(4))
            BEGIN                            
               DECLARE cc INT;

                SET npage=perpage*(npage-1);
               
                SELECT COUNT(*) INTO cc
                FROM clients c
    			WHERE c.deleted_at IS NULL
                AND IF(date_from IS NULL OR date_to IS NULL, TRUE, (DATE(c.created_at) >= date_from AND DATE(c.created_at) <= date_to))
                AND IF(_text IS NULL OR _text= '', TRUE, (c.first_name LIKE CONCAT('%',_text,'%')));

                SET @query = CONCAT("
                    SELECT c.id, c.first_name, c.created_at, c.updated_at, ", cc ," cc,
                    JSON_ARRAYAGG(JSON_OBJECT('id', b.id, 'name', b.name)) AS businesses
                    FROM clients c
                    LEFT JOIN businesses b ON c.id = b.client_id and b.deleted_at is null
                    WHERE c.deleted_at IS NULL",
                    IF (date_from IS NULL OR date_to IS NULL, '', CONCAT(" AND DATE(c.created_at) >= '",date_from, "' AND DATE(c.created_at) <= '", date_to, "'")),
                    IF(_text IS NULL OR _text = '', '', CONCAT(" AND c.first_name LIKE '%",_text,"%'")),
                    " GROUP BY c.id ORDER BY c.", order_by, " ", orden , " LIMIT ",perpage," OFFSET ",npage, ";");

                    PREPARE stmt FROM @query;
                    EXECUTE stmt;
                    DEALLOCATE PREPARE stmt;
            END;
        """)
    ]

