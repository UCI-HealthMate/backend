from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    day = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    period = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
