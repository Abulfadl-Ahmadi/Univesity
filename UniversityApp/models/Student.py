from django.db import models
from django import forms
from UniversityApp.enums import Gender
from django.utils import timezone


class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.IntegerField(max_length=2)
    email = models.EmailField(unique=True)
    tell_phone = models.CharField(max_length=13, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.female)
    grade = models.CharField(max_length=2, choices=Grade.choices, default=Grade.Freshman)
    term = models.CharField(max_length=1, choices=Term.choices, default=Term.One)
    birthdate = models.DateTimeField(default=timezone.now)


class Teacher(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)
    national_code = models.CharField(max_length=10, unique=True)
    age = models.IntegerField(max_length=3)
    email = models.EmailField(unique=True)
    tell_phone = models.CharField(max_length=13, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.male)
    grade = models.CharField(max_length=2, choices=Grade.choices, default=Grader.Master)
    birthdate = models.DateTimeField(default=timezone.now)
