from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Course

# Create your tests here.
class CourseTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@mail.com",
            password="sEcret123",
        )

        cls.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            teacher=cls.user,
        )

    def test_course_model(self):
        self.assertEqual(self.course.title, "Test Course")
        self.assertEqual(self.course.description, "Test Description")
        self.assertEqual(self.course.teacher.username, "testuser")