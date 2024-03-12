from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name', 'description', 'day', 'price', 'period', 'date']

class MenuRequestSerializer(serializers.Serializer):
    Calories = serializers.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    ContainsEggs = serializers.BooleanField(default=False)
    ContainsFish = serializers.BooleanField(default=False)
    ContainsMilk = serializers.BooleanField(default=False)
    ContainsPeanuts = serializers.BooleanField(default=False)
    ContainsSesame = serializers.BooleanField(default=False)
    ContainsShellfish = serializers.BooleanField(default=False)
    ContainsSoy = serializers.BooleanField(default=False)
    ContainsTreeNuts = serializers.BooleanField(default=False)
    ContainsWheat = serializers.BooleanField(default=False)
    IsGlutenFree = serializers.BooleanField(default=False)
    IsHalal = serializers.BooleanField(default=False)
    IsKosher = serializers.BooleanField(default=False)
    IsLocallyGrown = serializers.BooleanField(default=False)
    IsOrganic = serializers.BooleanField(default=False)
    IsVegan = serializers.BooleanField(default=False)
    IsVegetarian = serializers.BooleanField(default=False)