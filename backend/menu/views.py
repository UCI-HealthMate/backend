from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from menu.task import fetch_and_update_menu
from drf_yasg.utils import swagger_auto_schema

class Menu(APIView):
    @swagger_auto_schema(
        operation_description="Get Recommended Menu",
        responses={200: 'Menu fetched successfully', 400: 'Bad Request'}
    )
    def get(self, request):
        pass
    
    @swagger_auto_schema(
        operation_description="Update User Menu",
        responses={200: 'Menu updated successfully', 400: 'Bad Request'}
    )
    def post(self, request):
        pass

class Trigger(APIView):
    @swagger_auto_schema(
        operation_description="Trigger task",
        responses={200: 'Task triggered successfully', 400: 'Bad Request'}
    )
    def gets(self, request):
        fetch_and_update_menu.delay()
        return Response({'message': 'Task triggered successfully'}, status=status.HTTP_200_OK)