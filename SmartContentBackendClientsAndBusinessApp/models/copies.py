from django.db import models

class Copies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=360)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE, db_column='business_id')
    class Meta:
        db_table = 'copies'