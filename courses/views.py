from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Course, CourseWeek, CourseAttendance, CourseMaterial, CourseStudentsEnrolled
from .serializers import (CourseSerializer, CourseWeekSerializer, CourseAttendanceSerializer,
                          CourseMaterialSerializer, CourseStudentsEnrolledSerializer,
                          CourseCreateSerializer, CourseAttendanceCreateSerializer, CourseWeekCreateSerializer)
from .permissions import IsTeacherOrReadOnly, TeacherOnly

# Create your views here.
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseWeekList(generics.ListAPIView):
    serializer_class = CourseWeekSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseWeek.objects.filter(course__id=course_id)

class CourseWeekDetail(generics.RetrieveAPIView):
    queryset = CourseWeek.objects.all()
    serializer_class = CourseWeekSerializer


class CourseMaterialDetail(generics.RetrieveAPIView):
    serializer_class = CourseMaterialSerializer

    def get_object(self):
        course_id = self.kwargs['course_id']
        week = self.kwargs['week']
        return CourseMaterial.objects.get(course_week__course__id=course_id, course_week__week_number=week)

class CourseAttendanceList(generics.ListAPIView):
    serializer_class = CourseAttendanceSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        week = self.kwargs['week']
        return CourseAttendance.objects.filter(course_week__week_number=week, course_week__course__id=course_id)
    
    
class CourseAttendaceCreate(generics.CreateAPIView):
    queryset = CourseAttendance.objects.all()
    serializer_class = CourseAttendanceCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseEnrolledList(generics.ListAPIView):
    serializer_class = CourseStudentsEnrolledSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return CourseStudentsEnrolled.objects.filter(course__id=course_id)
    


class CourseCreate(generics.CreateAPIView):
    permission_classes = (TeacherOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

class CourseWeekCreate(generics.CreateAPIView):
    permission_classes = (TeacherOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseWeekCreateSerializer