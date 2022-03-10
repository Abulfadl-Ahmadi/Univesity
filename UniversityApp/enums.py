from django.db import models


class Gender(models.TextChoices):
    MALE = 'M', "Male"
    FEMALE = 'F', "Female"


class Term(models.TextChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'
    SIX = 6, 'Six'
    SEVEN = 7, 'Seven'
    EIGHT = 8, 'Eight'
    NINE = 9, 'Nine'
    TEN = 10, 'ten'
