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

class Items(APIView):
    @swagger_auto_schema(
        operation_description="Get Recommended Menu",
        responses={200: 'Menu fetched successfully', 400: 'Bad Request'}
    )
    def get(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        token = AccessToken(access_token)
        user_email = token['email']
        if user_email is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': f'user email for testing: {user_email}'}, status=status.HTTP_200_OK)
        
    
    @swagger_auto_schema(
        operation_description="Update User Menu",
        responses={200: 'Menu updated successfully', 400: 'Bad Request'}
    )
    def post(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        token = AccessToken(access_token)
        user_email = token['email']
        if user_email is None:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'message': f'user email for testing: {user_email}'}, status=status.HTTP_200_OK)

class Trigger(APIView):
    @swagger_auto_schema(
        operation_description="Trigger task",
        responses={200: 'Task triggered successfully', 400: 'Bad Request'}
    )
    def get(self, request):
        fetch_and_update_menu.delay()
        return Response({'message': 'Task triggered successfully'}, status=status.HTTP_200_OK)