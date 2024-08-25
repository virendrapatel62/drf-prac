from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courses')
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return f'{self.student.first_name} - {self.course.title}'
