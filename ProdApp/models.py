from django.db import models

# Create your models here.

class Product(models.Model):
    prod_id     = models.CharField(max_length=12,unique=True)
    prod_desc   = models.CharField(max_length=50,null=True,blank=True)
    uom         = models.CharField(max_length=5,null=True,blank=True)

    def __str__(self):
        return self.prod_id
    