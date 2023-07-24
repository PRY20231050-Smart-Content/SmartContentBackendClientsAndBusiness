from django.db import models

class PostTracking(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.DateTimeField()  # Supongo que este campo debería ser TextField y no DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.CharField(max_length=255)
    class Meta:
        db_table = 'post_tracking'