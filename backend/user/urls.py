from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'user'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', views.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
