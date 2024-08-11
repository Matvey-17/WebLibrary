from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=125, null=False, blank=False)
    author = models.CharField(max_length=125, null=False, blank=False)
    genre = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
