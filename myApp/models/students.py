from django.db import models
from django import forms
from courses import Course
from masters import Master
from myApp.enums import Gender
from addresses import Address
from phonenumber_field.modelfields import PhoneNumberField
from sections import Section
from degrees import DegreeLevel


class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=128, unique=True)
    password = forms.CharField(widget=forms.PasswordInput)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.PREFER_NOT_TO_RESPOND)
    national_code = models.CharField(max_length=10, unique=True)
    birthdate = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL)
    degree = models.ForeignKey(DegreeLevel, on_delete=models.PROTECT)


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    master = models.ForeignKey(Master, on_delete=models.SET_NULL)
