from django.urls import path

from .views import (CourseList, CourseDetail, CourseWeekList, 
                    CourseWeekDetail, CourseMaterialDetail,
                    CourseAttendanceList, CourseEnrolledList,
                    
                    CourseCreate, CourseAttendaceCreate)

urlpatterns = [
    path("", CourseList.as_view(), name="course_list"),
    path("<int:pk>/", CourseDetail.as_view(), name="course_detail"),
    path("<int:course_id>/weeks/", CourseWeekList.as_view(), name="course_week_list"),
    path("<int:course_id>/weeks/<int:pk>/", CourseWeekDetail.as_view(), name="course_week_detail"),
    path("<int:course_id>/weeks/<int:week>/materials/", CourseMaterialDetail.as_view(), name="course_material_detail"),
    path("<int:course_id>/weeks/<int:week>/attendances/", CourseAttendanceList.as_view(), name="course_attendances"),
    path("<int:course_id>/students/", CourseEnrolledList.as_view(), name="course_students"),

    path("create/", CourseCreate.as_view(), name="course_create"),
    path("<int:course_id>/weeks/<int:week>/attendances/create/", CourseAttendaceCreate.as_view(), name="course_attendances"),

]