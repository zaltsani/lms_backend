from django.urls import path

from .views import StudentCourseList

urlpatterns = [
    path('<int:student_id>/course/', StudentCourseList.as_view(), name='student_course'),
]