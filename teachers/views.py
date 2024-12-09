from rest_framework import generics

from courses.models import Course
from courses.serializers import CourseSerializer

# Create your views here.
class TeacherCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        return Course.objects.filter(teacher__id=teacher_id)