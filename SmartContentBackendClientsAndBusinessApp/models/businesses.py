from django.db import models

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=360)
    target_audience = models.TextField()
    experience_years = models.CharField(max_length=360)
    reach_range = models.IntegerField()
    phone = models.IntegerField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    website = models.CharField(max_length=360)
    mail = models.EmailField(max_length=100)
    industry = models.ForeignKey('Industry', on_delete=models.CASCADE)
    schedule = models.CharField(max_length=360)
    created_at = models.DateTimeField(auto_now_add=True)
    copy_languages = models.CharField(max_length=100)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    mission = models.TextField()
    vision = models.TextField()
    values = models.TextField()
    class Meta:
        db_table = 'businesses'