from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)
    languages = models.JSONField()

    def __str__(self):
        return self.country