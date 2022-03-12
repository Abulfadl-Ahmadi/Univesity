from django.db import models
from universities import University


class Department(models.Model):
    title = models.CharField(max_length=150)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
