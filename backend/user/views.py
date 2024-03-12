from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema

class Signup(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            response = Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
            response.set_cookie('access_token', str(access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh_token), httponly=True)
            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
