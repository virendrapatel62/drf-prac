from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=500,  blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    discount = models.IntegerField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=200, blank=False, null=False)
