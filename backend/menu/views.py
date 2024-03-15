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
from .algorithm import find_menu_combinations, calculate_bmr, rank_menu_combinations, distribute_calories_with_brunch, distribute_calories_with_late, get_top_3_combinations

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
            return Response({'error': 'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
        if user_id is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)
        options = ["Breakfast", "Brunch", "Lunch", "Dinner", "Late"]
        menu_dict = {}
        user_data = request.query_params
        bmr = calculate_bmr(user_data['sex'], user_data['age'], user_data['height'], user_data['weight'], user_data['timeInBed'],user_data['calories'])
        if Menu.objects.filter(period="Brunch").exists():
            options = ["Breakfast", "Brunch", "Dinner"]
            distributed_calories = distribute_calories_with_brunch(bmr)
        elif Menu.objects.filter(period="Lunch").exists():
            options = ["Breakfast", "Lunch", "Dinner", "Late"]
            distributed_calories = distribute_calories_with_late(bmr)

        for period_option in options:
            period_menus = {}
            
            qualified_menu_items = Menu.objects.filter(
                period=period_option,
                containsEggs=user_data['containsEggs'],
                containsFish=user_data['containsFish'],
                containsMilk=user_data['containsMilk'],
                containsPeanuts=user_data['containsPeanuts'],
                containsSesame=user_data['containsSesame'],
                containsShellfish=user_data['containsShellfish'],
                containsSoy=user_data['containsSoy'],
                containsTreeNuts=user_data['containsTreeNuts'],
                containsWheat=user_data['containsWheat'],
                isGlutenFree=user_data['isGlutenFree'],
                isHalal=user_data['isHalal'],
                isKosher=user_data['isKosher'],
                isVegan=user_data['isVegan'],
                isVegetarian=user_data['isVegetarian']
            )
            combos = find_menu_combinations(qualified_menu_items, distributed_calories[period_option], 5)
            ranked_combos = rank_menu_combinations(combos, distributed_calories[period_option])
            top_3_combos = get_top_3_combinations(ranked_combos)
                
            period_menus["1"] = top_3_combos[0]
            period_menus["2"] = top_3_combos[1]
            period_menus["3"] = top_3_combos[2]
                
            menu_dict[period_option] = period_menus

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