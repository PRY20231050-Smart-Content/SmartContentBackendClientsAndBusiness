from django.db import models

class Industry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'industries'