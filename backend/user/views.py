from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,status,views,permissions
from .serializers import SignupSerializer,LoginSerializer,LogoutSerializer
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class Signup(generics.GenericAPIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            
            serializer.validated_data['created_at'] = timezone.now()
            serializer.validated_data['updated_at'] = timezone.now()
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)