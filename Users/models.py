from django.db import models
from django.contrib.auth.models import AbstractUser
from Library.models import Book
import datetime


class User(AbstractUser):
    ROLE = {
        'R': 'Reader',
        'L': 'Librian'
    }

    books = models.ManyToManyField(Book, through='Enrollment')
    personnel_number = models.CharField(max_length=50, blank=True, null=True, unique=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=5, choices=ROLE, default='R')


class Enrollment(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return f'{self.reader.username} | {self.book.name}'
