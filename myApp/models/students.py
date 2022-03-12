from django.db import models
from django import forms
from courses import Course
from masters import Master


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=128, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)
    email = models.EmailField()
    national_code = models.CharField(max_length=10, unique=True)
    birthdate = models.DateField()


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    master = models.ForeignKey(Master, on_delete=models.SET_NULL())
