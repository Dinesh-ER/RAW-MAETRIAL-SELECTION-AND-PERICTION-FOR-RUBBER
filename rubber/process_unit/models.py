from django.db import models

# Create your models here.


class unit_register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact_no = models.PositiveBigIntegerField()
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class analyse_rubber(models.Model):
    property = models.CharField(max_length=200)
    recycle = models.CharField(max_length=200)
    compound = models.CharField(max_length=200)
    chemical_formula = models.CharField(max_length=200)
    polymer = models.CharField(max_length=200)
    mixing = models.CharField(max_length=200)
    made_from_type = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    send_analyse = models.BooleanField(default=False)
    rubber_type = models.CharField(max_length=200, null=True)
    send_report = models.BooleanField(default=False)


class testing_rubber(models.Model):
    property = models.CharField(max_length=200)
    recycle = models.CharField(max_length=200)
    compound = models.CharField(max_length=200)
    chemical_formula = models.CharField(max_length=200)
    polymer = models.CharField(max_length=200)
    mixing = models.CharField(max_length=200)
    made_from_type = models.CharField(max_length=200)
    type = models.CharField(max_length=200, null=True)
    output = models.CharField(max_length=200, null=True)
    matching = models.BooleanField(default=False)
    send_testing = models.BooleanField(default=False)
    send_matching = models.BooleanField(default=False)


