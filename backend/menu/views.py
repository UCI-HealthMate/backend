from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

periodMap = {
    "107" : "dinner",
    "49" : "breakfast",
    "106" : "lunch",
    "2651" : "brunch",
    "108" : "late night",
}

class Menu(APIView):
    def get(self, request):
        pass
