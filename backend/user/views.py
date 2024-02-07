from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # Check if email and confirm_email match
        if serializer.validated_data['email'] != serializer.validated_data['confirm_email']:
            return Response({'error': 'Email addresses do not match'}, status=400)
        # Check if password and confirm_password match
        if serializer.validated_data['password'] != serializer.validated_data['confirm_password']:
            return Response({'error': 'Passwords do not match'}, status=400)
        
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)