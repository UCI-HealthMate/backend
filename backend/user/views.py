from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class Signup(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            
            # Optionally add created_at and updated_at timestamps
            serializer.validated_data['created_at'] = timezone.now()
            serializer.validated_data['updated_at'] = timezone.now()
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
