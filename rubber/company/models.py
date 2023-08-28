from django.db import models

# Create your models here.


class co_register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact_no = models.PositiveBigIntegerField()
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


class natural_rubber(models.Model):
    latex_method = models.CharField(max_length=200)
    latex_char = models.CharField(max_length=200)
    acid = models.CharField(max_length=200)
    Time_taken = models.PositiveIntegerField(null=True)
    polymer = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    type_of_trees = models.CharField(max_length=200)
    type_of_plants = models.CharField(max_length=200)
    property = models.CharField(max_length=200)
    send_natural = models.BooleanField(default=False)
    need_latex = models.PositiveIntegerField(null=True)
    availability = models.PositiveIntegerField(null=True)
    remaining = models.PositiveIntegerField(null=True)
    check_remaining = models.BooleanField(default=False)
    fixing_date = models.CharField(max_length=200, null=True)
    send_fixing_date = models.BooleanField(default=False)
    natural_id = models.IntegerField(null=True)
    email = models.EmailField(null=True, unique=True)
    give_vendor = models.EmailField(null=True, unique=True)
    send_process_nal = models.BooleanField(default=False)


class synthetic_rubber(models.Model):
    industry = models.CharField(max_length=200)
    property = models.CharField(max_length=200)
    polymer_type = models.CharField(max_length=200)
    mineral_type = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    gases = models.CharField(max_length=200)
    storage_type = models.CharField(max_length=200)
    chemical_type = models.CharField(max_length=200)
    rubber_type = models.CharField(max_length=200)
    duration = models.CharField(max_length=200,null=True)
    send_synthetic = models.BooleanField(default=False)
    need_chemical = models.CharField(max_length=200, null=True)
    availability = models.CharField(max_length=200, null=True)
    remaining = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    syn_id = models.CharField(max_length=200, null=True)
    give_vendor_email = models.EmailField(unique=True, null=True)
    check_remaining1 = models.BooleanField(default=False)
    fixing_date1 = models.CharField(max_length=200, null=True)
    send_fixing_date1 = models.BooleanField(default=False)
    send_process_syn = models.BooleanField(default=False)







