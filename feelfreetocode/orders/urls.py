
from django.urls import path, include

from rest_framework import routers
from .views import EnrollMentCreateApiView, EnrollMentListApiView, EnrollmentRetrieveApiView


app_name = 'enrollments'


urlpatterns = [
    path('', EnrollMentListApiView.as_view(), name='enrollment-list'),
    path('create/', EnrollMentCreateApiView.as_view(), name='enrollment-create'),
    path('<int:pk>/', EnrollmentRetrieveApiView.as_view(),
         name='enrollment-retrieve')
]
