from django.db import models

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=360)
    target_audience = models.TextField()
    facebook_page = models.CharField(max_length=360)
    phone = models.TextField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    website = models.CharField(max_length=360)
    mail = models.EmailField(max_length=100)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    schedule = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    mission = models.TextField()
    vision = models.TextField()
    logo_carpet = models.TextField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    class Meta:
        db_table = 'businesses'