from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    # day = models.CharField(max_length=2)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    period = models.CharField(max_length=25)
    containsEggs = models.BooleanField()
    containsFish = models.BooleanField()
    containsMilk = models.BooleanField()
    containsPeanuts = models.BooleanField()
    containsSesame = models.BooleanField()
    containsShellfish = models.BooleanField()
    containsSoy = models.BooleanField()
    containsTreeNuts = models.BooleanField()
    containsWheat = models.BooleanField()
    isGlutenFree = models.BooleanField()
    isHalal = models.BooleanField()
    isKosher = models.BooleanField()
    isVegan = models.BooleanField()
    isVegetarian = models.BooleanField()
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    caloriesFromFat = models.DecimalField(max_digits=6, decimal_places=2)
    totalFat = models.DecimalField(max_digits=6, decimal_places=2)
    transFat = models.DecimalField(max_digits=6, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    sodium = models.DecimalField(max_digits=6, decimal_places=2)
    totalCarbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    sugars = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    vitaminA = models.DecimalField(max_digits=6, decimal_places=2)
    vitaminC = models.DecimalField(max_digits=6, decimal_places=2)
    calcium = models.DecimalField(max_digits=6, decimal_places=2)
    iron = models.DecimalField(max_digits=6, decimal_places=2)
    saturatedFat = models.DecimalField(max_digits=6, decimal_places=2)                                
    date = models.DateField()
    
    def __str__(self):
        return self.name