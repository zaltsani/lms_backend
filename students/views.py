from rest_framework import generics

from courses.models import CourseStudentsEnrolled
from courses.serializers import CourseStudentsEnrolledSerializer

# Create your views here.
class StudentCourseList(generics.ListAPIView):
    serializer_class = CourseStudentsEnrolledSerializer
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return CourseStudentsEnrolled.objects.filter(student__id=student_id)