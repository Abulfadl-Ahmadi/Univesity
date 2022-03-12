from django.db import models


class University(models.Model):
    name = models.CharField(max_length=150)
