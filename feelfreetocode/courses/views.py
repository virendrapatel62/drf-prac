from django.shortcuts import render
from .models import Course
from rest_framework.response import Response
from .serializers import CourseSerializer


from rest_framework.decorators import api_view


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, pk):
    course = Course.objects.get(pk=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
