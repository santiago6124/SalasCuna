from rest_framework import permissions


class DirectorPerms(permissions.BasePermission):
    message = "Solo las personas con rol Directora pueden acceder a esta información"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Director").exists():
            print("Si podes entrar")
            return request.method
        else:
            print("No flaco, cagate")
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Director").exists():
            return True
        else:
            return False


class TrabajadorSocialPerms(permissions.BasePermission):
    message = (
        "Solo las personas con rol Trabajador Social pueden acceder a esta información"
    )

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Trabajador Social").exists():
            print("Si podes entrar")
            return request.method
        else:
            print("No flaco, cagate")
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Trabajador Social").exists():
            return True
        else:
            return False
