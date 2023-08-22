from django.contrib import admin
from .models import *

# Register your models here.


class LocalityAdmin(admin.ModelAdmin):
    list_display = ("id", "locality")
    list_filter = ["locality"]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "department")
    list_filter = ["department"]

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ("id", "neighborhood")
    list_filter = ["neighborhood"]


class ChildAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "dni", "cribroom", "guardian")
    list_filter = ["last_name", "cribroom"]
    search_fields = ["last_name", ""]


class ChildStateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "phone")
    list_filter = ["title"]


class CribroomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "locality", "zone", "shift")
    list_filter = ["name", "code", "locality"]


class CribroomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom", "user")
    list_filter = ["cribroom", "user"]


class DesinfectionAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom", "company", "date")
    list_filter = ["cribroom", "company"]


class FormAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom_user", "role")
    list_filter = ["cribroom_user"]


class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "gender")
    list_filter = ["gender"]


class PhoneFeatureAdmin(admin.ModelAdmin):
    list_display = ("id", "feature")
    list_filter = ["feature"]


class GuardianTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    list_filter = ["type"]


class GuardianAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "dni", "guardian_Type")
    list_filter = ["last_name", "guardian_Type"]


class PayoutAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date")
    list_filter = ["amount", "date"]


class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "gender")
    list_filter = ["gender"]


class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class ShiftAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "email", "role")
    list_filter = [
        "role",
        "email",
    ]


class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


admin.site.register(Child, ChildAdmin)
admin.site.register(ChildState, ChildStateAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Cribroom, CribroomAdmin)
admin.site.register(CribroomUser, CribroomUserAdmin)
admin.site.register(Desinfection, DesinfectionAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(PhoneFeature, PhoneFeatureAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(GuardianType, GuardianTypeAdmin)
admin.site.register(Payout, PayoutAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Zone, ZoneAdmin)
