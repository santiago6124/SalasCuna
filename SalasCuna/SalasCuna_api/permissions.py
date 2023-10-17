from rest_framework import permissions


class AllUsersPerms(permissions.BasePermission):
    message = "All user has access to this information"

    def has_permission(self, request, view):
        if request.user.id is not None:
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.id is not None:
            return True
        else:
            return False


class DevPerms(permissions.BasePermission):
    message = "Solo developers"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="Dev").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="Dev").exists():
            return True
        else:
            return False


class DirectorPerms(permissions.BasePermission):
    message = "Solo las personas con rol Director pueden acceder a esta información"

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


class CoordinadorTSPerms(permissions.BasePermission):
    message = (
        "Solo las personas con rol CoordinadorTS pueden acceder a esta información"
    )

    def has_permission(self, request, view):
        if request.user.groups.filter(name="CoordinadorTS").exists():
            return request.method
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name="CoordinadorTS").exists():
            return True
        else:
            return False
