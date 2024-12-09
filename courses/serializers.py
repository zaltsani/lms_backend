from rest_framework import serializers

from .models import Course, CourseWeek, CourseMaterial, CourseStudentsEnrolled, CourseAttendance
from accounts.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "teacher",
        )
        model = Course

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseWeekSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = CourseWeek
        fields = '__all__'

class CourseMaterialSerializer(serializers.ModelSerializer):
    course_week = CourseWeekSerializer()
    class Meta:
        model = CourseMaterial
        fields = '__all__'

class CourseStudentsEnrolledSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = UserSerializer()
    class Meta:
        model = CourseStudentsEnrolled
        fields = (
            'id',
            'course',
            'student',
        )

class CourseAttendanceSerializer(serializers.ModelSerializer):
    course_week = CourseWeekSerializer()
    student = UserSerializer()
    class Meta:
        model = CourseAttendance
        fields = '__all__'

class CourseAttendanceCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CourseAttendance
        fields = '__all__'

class CourseAttendanceCreateListSerializer(serializers.ListSerializer):
    child = CourseAttendanceCreateSerializer()

    def create(self, validated_data):
        course_attendance_list = []
        for item in validated_data:
            course_attendance = CourseAttendance.objects.create(**item)
            course_attendance_list.append(course_attendance)
        return course_attendance_list
    
class CourseWeekCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseWeek
        fields = '__all__'