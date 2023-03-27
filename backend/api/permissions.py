from rest_framework import permissions


class IsAdminrPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff)

    def has_permission(self, request, view):
        return (request.user.is_staff)
