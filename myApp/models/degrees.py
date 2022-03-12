from django.db import models
from myApp.enums import DegreeLevel


def gpa(grade):
    if 18 <= grade <= 20:
        return 'A'
    elif 17 <= grade < 18:
        return 'B+'
    elif 16 <= grade < 17:
        return 'B'
    elif 14 <= grade < 16:
        return 'C+'
    elif 12 <= grade < 14:
        return 'C'
    elif 10 <= grade < 12:
        return 'D'
    elif 0 <= grade < 10:
        return'F'


class Degree(models.Model):
    degree_name = models.CharField(max_length=150)
    level = models.CharField(max_length=1, choices=DegreeLevel.choices)
    grade = models.PositiveSmallIntegerField()
    # gpa = gpa(grade)  # grade point average
