from django.urls import path
from .views import Trigger, Menu

urlpatterns = [
    path('trigger/', Trigger.as_view(), name='trigger_task'),
    path('menu/', Menu.as_view(), name='menu'),
]