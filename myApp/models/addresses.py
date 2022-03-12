from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    county = models.CharField(max_length=150)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length=150)
