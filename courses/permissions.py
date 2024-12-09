from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.teacher == request.user
    
class TeacherOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff