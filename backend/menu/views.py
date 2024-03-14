from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
# from django.utils import timezone
from menu.task import fetch_and_update_menu
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import AccessToken
from user.models import User
from .parameters import menu_parameters
from .models import Menu

class Items(APIView):
    @swagger_auto_schema(
        operation_description="Get Recommended Menu",
        manual_parameters=menu_parameters,
        responses={200: 'Menu fetched successfully', 400: 'Bad Request'}
    )
    def get(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        token = AccessToken(access_token)
        token_data = token.payload
        user_id = token_data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
        if user_id is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)
        options = ["Breakfast", "Brunch", "Lunch", "Dinner", "Late"]
        menu_dict = {}

        for period in options:
            # Initialize an empty dictionary for the period
            period_menus = {}
            
            # Get the menu objects for the period
            if Menu.objects.filter(period=period).exists():
                menu_objects = Menu.objects.filter(period=period).order_by('?')[:5]
                
                # Initialize an empty list for the menu items
                menu_items = []
                
                # Populate the menu items list with menu objects
                for menu_obj in menu_objects:
                    menu_item = {
                        "id": menu_obj.id,
                        "name": menu_obj.name,
                        "description": menu_obj.description,
                        "containsEggs": menu_obj.containsEggs,
                        "containsFish": menu_obj.containsFish,
                        "containsMilk": menu_obj.containsMilk,
                        "containsPeanuts": menu_obj.containsPeanuts,
                        "containsSesame": menu_obj.containsSesame,
                        "containsShellfish": menu_obj.containsShellfish,
                        "containsSoy": menu_obj.containsSoy,
                        "containsTreeNuts": menu_obj.containsTreeNuts,
                        "containsWheat": menu_obj.containsWheat,
                        "isGlutenFree": menu_obj.isGlutenFree,
                        "isHalal": menu_obj.isHalal,
                        "isKosher": menu_obj.isKosher,
                        "isVegan": menu_obj.isVegan,
                        "isVegetarian": menu_obj.isVegetarian,
                        "calories": menu_obj.calories,
                        "caloriesFromFat": menu_obj.caloriesFromFat,
                        "totalFat": menu_obj.totalFat,
                        "transFat": menu_obj.transFat,
                        "cholesterol": menu_obj.cholesterol,
                        "sodium": menu_obj.sodium,
                        "totalCarbohydrates": menu_obj.totalCarbohydrates,
                        "sugars": menu_obj.sugars,
                        "protein": menu_obj.protein,
                        "vitaminA": menu_obj.vitaminA,
                        "vitaminC": menu_obj.vitaminC,
                        "calcium": menu_obj.calcium,
                        "iron": menu_obj.iron,
                        "saturatedFat": menu_obj.saturatedFat,
                        "station": menu_obj.station
                    }
                    menu_items.append(menu_item)
                
                # Populate the period dictionary with three ranks having the same menu items
                period_menus["rank1"] = menu_items
                period_menus["rank2"] = menu_items
                period_menus["rank3"] = menu_items
                
                # Assign the period dictionary to the menu_dict
                menu_dict[period] = period_menus

        # Return the menu_dict in the response
        return Response(menu_dict, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description="Update User Menu",
        responses={200: 'Menu updated successfully', 400: 'Bad Request'}
    )
    def post(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        token = AccessToken(access_token)
        token_data = token.payload
        user_id = token_data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
        if user_id is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': f'user email for testing: {user.email}'}, status=status.HTTP_200_OK)

class Trigger(APIView):
    @swagger_auto_schema(
        operation_description="Trigger task",
        responses={200: 'Task triggered successfully', 400: 'Bad Request'}
    )
    def get(self, request):
        fetch_and_update_menu.delay()
        return Response({'message': 'Task triggered successfully'}, status=status.HTTP_200_OK)