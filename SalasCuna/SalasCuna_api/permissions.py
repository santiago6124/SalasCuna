from rest_framework import permissions


class DirectorPerms(permissions.BasePermission):
    message = "Solo las personas con rol Directora pueden acceder a esta información"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Director").exists():
            return request.method
        else:
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
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Trabajador Social").exists():
            return True
        else:
            return False


class ArquitectoPerms(permissions.BasePermission):
    message = "Solo las personas con rol Arquitecto pueden acceder a esta información"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Arquitecto").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Arquitecto").exists():
            return True
        else:
            return False


class PsicopedagogaPerms(permissions.BasePermission):
    message = (
        "Solo las personas con rol Psicopedagoga pueden acceder a esta información"
    )

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Psicopedagoga").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Psicopedagoga").exists():
            return True
        else:
            return False


class AdministradorPerms(permissions.BasePermission):
    message = (
        "Solo las personas con rol Administrador pueden acceder a esta información"
    )

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Administrador").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Administrador").exists():
            return True
        else:
            return False


class SecretarioPerms(permissions.BasePermission):
    message = "Solo las personas con rol Secretario pueden acceder a esta información"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Secretario").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Secretario").exists():
            return True
        else:
            return False
