from django.urls import path

from .views import TeacherCourseList

urlpatterns = [
    path("<int:teacher_id>/course/", TeacherCourseList.as_view(), name='teacher_course_list'),
]