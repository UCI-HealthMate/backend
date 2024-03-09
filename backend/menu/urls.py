from django.urls import path
from .views import trigger_task

urlpatterns = [
    path('trigger/', trigger_task, name='trigger_task'),
    # Other URL patterns...
]