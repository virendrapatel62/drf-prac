
from django.urls import path, include

from rest_framework import routers


# from .views import CourseListCreateApiView, CourseDestroyApiView
from .views import CourseViewSet

app_name = 'courses'


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', CourseViewSet)


urlpatterns = [
    # path('', CourseListCreateApiView.as_view(), name='course-list'),
    # path('<int:pk>/', CourseDestroyApiView.as_view(), name='course-list')
    path('', include(router.urls))

]
