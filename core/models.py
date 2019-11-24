from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.CharField(max_length=150)
    shorten_url = models.CharField(max_length=10, default=None, blank=True, null=True)