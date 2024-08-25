
from django.urls import path, include
from .views import get_courses, get_course


app_name = 'courses'


urlpatterns = [
    path('', get_courses),
    path('<pk:int>', get_course)
]
