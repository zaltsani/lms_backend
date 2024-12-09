from django.urls import path, include

from .views import Me, UserDetail


urlpatterns = [
    path('me/', Me.as_view(), name="me"),
    path('', UserDetail.as_view(), name="user-detail")
]