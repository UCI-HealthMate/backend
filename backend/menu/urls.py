from django.urls import path
from .views import Trigger, Items

urlpatterns = [
    path('trigger/', Trigger.as_view(), name='trigger_task'),
    path('items/', Items.as_view(), name='items'),
]