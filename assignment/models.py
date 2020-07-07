from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = ( 
    ("MALE", "Male"),
    ("FELAME", "Female"),
    ("OTHER", "Other"),
) 

class Address(models.Model):
    streetAddress = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.streetAddress

class User(AbstractUser):
    phoneNumber = models.CharField(unique=True, max_length=10)
    gender = GENDER_CHOICES
    profilePic = models.ImageField(upload_to='uploads/', null=True)
    dob = models.DateField(null=True)
    permanentAddress = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    # companyAddress = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.phoneNumber