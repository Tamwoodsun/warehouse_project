from django.db import models
from warehouse.models import Warehouse
# Create your models here.

class Transfer(models.Model):
    user = models.CharField(max_length=200)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)
    rent_date = models.DateTimeField()
    end_date = models.DateTimeField()
    rent_paid = models.FloatField()
    is_active = models.BooleanField(default=True)
    note = models.TextField(null=True)
    
    def __str__(self):
        return str(self.warehouse)    