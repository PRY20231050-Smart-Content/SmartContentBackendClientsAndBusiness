from django.db import models

class BusinessAddressPreferences(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    class Meta:
        db_table = 'businesses_address_preferences'