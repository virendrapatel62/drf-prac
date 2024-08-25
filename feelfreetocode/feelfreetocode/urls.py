
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

urlpatterns = [
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
