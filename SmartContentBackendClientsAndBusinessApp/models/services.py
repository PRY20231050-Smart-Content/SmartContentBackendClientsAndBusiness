from django.db import models

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=360)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True)  # Alma
    
    class Meta:
        db_table = 'services'

            