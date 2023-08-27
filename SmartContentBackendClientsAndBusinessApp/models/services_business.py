from django.db import models

class CostLevel(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'

class ServiceBusiness(models.Model):
    id = models.AutoField(primary_key=True)
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE, db_column='business_id')
    service_id = models.ForeignKey('Service', on_delete=models.CASCADE, db_column='service_id')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=255)
    level_importance = models.IntegerField()

    class Meta:
        db_table = 'services_business'
