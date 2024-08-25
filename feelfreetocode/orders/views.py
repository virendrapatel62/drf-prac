from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentRetrieveApiView(generics.RetrieveAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class EnrollMentListApiView(generics.ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]


class EnrollMentCreateApiView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdminUser]
