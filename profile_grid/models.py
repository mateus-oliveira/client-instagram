from django.db import models

class User(models.Model):
    id_instagram = models.IntegerField(null=False, blank=False)
    username = models.CharField(max_length=100, null=False, blank=False)
    token = models.CharField(max_length=200, null=False, blank=False)