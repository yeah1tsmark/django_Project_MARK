from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    room = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50)
    date = models.CharField(max_length=50)


def __str__(self):
    return self.name
