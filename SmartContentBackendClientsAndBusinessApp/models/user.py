from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password_hash = models.CharField(max_length=255)
    STATUS_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    profile_picture = models.CharField(max_length=255,null=True)  # Considera usar ImageField si es una imagen
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
