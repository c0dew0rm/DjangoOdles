from django.db import models

# Create your models here.

class Address(models.Model):
    streetAddress = models.CharField(blank=True, max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.streetAddress