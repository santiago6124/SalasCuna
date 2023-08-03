from rest_framework import permissions


class IsTrabajadoraSocial(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.UserAccount.role.filter(name="Trabajadora Social").exists():
            return True
        else:
            return False
