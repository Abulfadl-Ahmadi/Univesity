from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=150)
    capacity = models.PositiveIntegerField()
    no_of_student = models.PositiveIntegerField()
