from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }