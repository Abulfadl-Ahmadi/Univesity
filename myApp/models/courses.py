from django.db import models
from departments import Department


class Course(models.Model):
    title = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    prerequisite = models.ForeignKey('Course', on_delete=models.SET_NULL)
