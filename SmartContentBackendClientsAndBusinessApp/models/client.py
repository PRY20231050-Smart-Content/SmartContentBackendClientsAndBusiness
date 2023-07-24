from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_id = models.ForeignKey('Address', on_delete=models.CASCADE, db_column='address_id')
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    profile_picture = models.CharField(max_length=255)  # Considera usar ImageField si es una imagen
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'clients'
