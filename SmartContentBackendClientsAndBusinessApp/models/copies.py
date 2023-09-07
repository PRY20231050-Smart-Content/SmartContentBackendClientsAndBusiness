from django.db import models

class Copies(models.Model):
    id = models.AutoField(primary_key=True)
    copy = models.TextField(null=True)
    likes = models.TextField(null=True)
    shared = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE, db_column='business_id')
    class Meta:
        db_table = 'copies'