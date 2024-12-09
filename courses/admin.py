from django.contrib import admin

from .models import Course, CourseWeek, CourseMaterial, CourseStudentsEnrolled, CourseAttendance

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseWeek)
admin.site.register(CourseMaterial)
admin.site.register(CourseStudentsEnrolled)
admin.site.register(CourseAttendance)