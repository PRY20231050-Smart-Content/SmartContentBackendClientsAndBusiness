from django.db import models

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=50)
    street = models.CharField(max_length=255)

    class Meta:
        db_table = 'address'
