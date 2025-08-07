from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.language


class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.country



