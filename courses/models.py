from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class CourseWeek(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='weeks')
    week_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = ('course', 'week_number')

    def __str__(self):
        return f"Week {self.week_number} - {self.title}"
    
    
class CourseMaterial(models.Model):
    course_week = models.ForeignKey(CourseWeek, on_delete=models.CASCADE, related_name="materials")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(blank=True, upload_to='course_materials/')

    def __str__(self):
        return self.title
    
class CourseAttendance(models.Model):
    course_week = models.ForeignKey(CourseWeek, on_delete=models.CASCADE, related_name="attendances")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendances")
    is_present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('course_week', 'student')

    def __str__(self):
        return f"{self.student.username} - {self.course_week} - {'Present' if self.is_present else 'Absent'}"
    
class CourseStudentsEnrolled(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')

    class Meta:
        unique_together = ('course', 'student')
    
    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"