from django.db import models

# Create your models here.


class register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact_no = models.PositiveBigIntegerField()
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    vendor_approve = models.BooleanField(default=False)
    graph1 = models.BooleanField(default=False)
    graph2 = models.BooleanField(default=False)
    graph3 = models.BooleanField(default=False)

