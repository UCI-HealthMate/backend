from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from .models import User

class Signup(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            user = User.objects.filter(email=request.data.get('email')).first()
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)
            response = Response({"message": "User created and logged in successfully"}, status=status.HTTP_201_CREATED)
            response.set_cookie('access_token', str(access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh_token), httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if user:
            if not check_password(password, user.password):
                return Response({'error': 'Invalid Password'}, status=status.HTTP_401_UNAUTHORIZED)
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            response = Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
            response.set_cookie('access_token', str(access_token), httponly=True)
            response.set_cookie('refresh_token', str(refresh_token), httponly=True)
            return response
        else:
            return Response({'error': 'Invalid User'}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        response = Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
