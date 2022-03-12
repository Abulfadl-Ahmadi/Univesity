from django.db import models


class Gender(models.TextChoices):
    FEMALE = 'F', 'Female '
    MALE = 'M', 'Male'
    TRANSGENDER = 'T', 'Transgender'
    NON_BINARY = 'N', 'Non - binary / non - conforming'
    PREFER_NOT_TO_RESPOND = 'P', 'Prefer not to respond'


