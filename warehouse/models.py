from django.db import models
from warehouse.choices import *
from autoslug import AutoSlugField
# Create your models here.

class Warehouse(models.Model):
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=50, choices=region_choices.items())
    district = models.CharField(max_length=50, choices=district_choices.items())
    street = models.CharField(max_length=200, null=True)
    building = models.CharField(max_length=200, null=True)
    floor = models.IntegerField()
    room = models.CharField()
    description = models.TextField()
    phone = models.CharField()
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    threemonrent = models.DecimalField(decimal_places=2, max_digits=7)
    sixmonrent = models.DecimalField(decimal_places=2, max_digits=7)
    ninemonrent = models.DecimalField(decimal_places=2, max_digits=7)
    is_listed = models.BooleanField()
    slug = AutoSlugField(populate_from='title',unique=True, null=True, default=None)
    
    def __str__(self):
        return str(self.title)
    
    def slugify_function(self, content):
        return content.replace('_', '-').lower()
    
    