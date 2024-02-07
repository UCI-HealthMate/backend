from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    confirm_email = models.EmailField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)