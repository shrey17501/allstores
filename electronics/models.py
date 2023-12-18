from django.db import models
from django.utils import timezone
# Create your models here.
    
class Electronic(models.Model):
    brand = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    store_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=600, null=True)
    mobile = models.CharField(max_length=300, null=True)
    operating_time = models.CharField(max_length=400, null=True)
    lat = models.CharField(max_length=30, null=True)
    lon = models.CharField(max_length=30, null=True)
    pin_code = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    brand_logo = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.brand
    
class Client(models.Model):
    email = models.CharField(max_length= 100, null= True)
    phone = models.CharField(max_length= 10, null= True)
    password = models.CharField(max_length=100, null= True)
    date  = models.DateField(default=timezone.now)

    def __str__(self):
        return self.email
    

class Supermarket(models.Model):
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    lon = models.CharField(max_length=30)
    store_type = models.CharField(max_length=30)

    def __str__(self):
        return self.store_name

class Movietheater(models.Model):
    brand_name = models.CharField(max_length=50)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    pin_code = models.CharField(max_length=15)
    lat = models.CharField(max_length=30)
    lon = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name
    
class Telecom(models.Model):
    store_type = models.CharField(max_length=250, null=True)
    store_name = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=400, null=True)
    phone = models.CharField(max_length=15, null=True)
    operating_time = models.CharField(max_length=300, null=True)
    lat = models.CharField(max_length=30, null=True)
    lon = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    brand_name = models.CharField(max_length=100, null=True)
    pincode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.brand_name
    
class Automobile(models.Model):
    dealership_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=500, null=True)
    phone = models.CharField(max_length=30, null=True)
    brand_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    lat = models.CharField(max_length=30, null=True)
    lon = models.CharField(max_length=30, null=True)
    pincode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.brand_name
