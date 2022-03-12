from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

