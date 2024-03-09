from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from menu.task import fetch_and_update_menu

@api_view(['POST', 'GET'])
def trigger_task(request):
    fetch_and_update_menu.delay()
    return Response({'message': 'Task triggered successfully'}, status=status.HTTP_200_OK)

# periodMap = {
#     "107" : "dinner",
#     "49" : "breakfast",
#     "106" : "lunch",
#     "2651" : "brunch",
#     "108" : "late night",
# }

# class Menu(APIView):
#     def get(self, request):
#         pass
