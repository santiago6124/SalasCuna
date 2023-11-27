from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import *


# Register your models here.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    # to filter the resultes by users, content types and action flags
    list_filter = ["user", "content_type", "action_flag"]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = ["object_repr", "change_message"]

    list_display = [
        "action_time",
        "user",
        "content_type",
        "action_flag",
    ]


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
    list_display = ("id", "__str__", "identification", "ident_type", "cribroom", "guardian")
    list_filter = ["last_name", "cribroom"]
    search_fields = ["last_name", ""]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "phone")
    list_filter = ["title"]


class CribroomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "max_capacity", "locality", "shift")
    list_filter = ["name", "code", "locality"]


class CribroomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom", "user")
    list_filter = ["cribroom", "user"]


class DesinfectionAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom", "company", "date")
    list_filter = ["cribroom", "company"]


class FormAdmin(admin.ModelAdmin):
    list_display = ("id", "cribroom_user")
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
    list_display = ("id", "__str__", "identification", "guardian_Type")
    list_filter = ["last_name", "identification", "guardian_Type"]


class PayoutAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "date")
    list_filter = ["amount", "date"]


class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "gender")
    list_filter = ["gender"]


class ShiftAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "email")
    list_filter = [
        "email",
    ]

class ZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]

class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "phone_name", "phone_Feature", "guardian")
    list_filter = ["guardian"]

class Co_managementAdmin(admin.ModelAdmin):
    list_display = ("id", "co_management")
    list_filter = [ "co_management"]

class SectionalAdmin(admin.ModelAdmin):
    list_display = ("id", "sectional")
    list_filter = ["sectional"]

class IdentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type")
    list_filter = ["type"]



class PollAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ["name"]

class ChildAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "child", 'answer', 'value')
    list_filter = ["child", 'answer', 'value']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "parentQuestion", "questionType", "poll")
    list_filter = ["description"]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "question", "answerType")
    list_filter = ["description"]

class TechnicalReportAdmin(admin.ModelAdmin):
    list_display = ("id", "encabezado", "ministro", "resolucion", "remitanse")
    list_filter = ["id"]

admin.site.register(Payout, PayoutAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Cribroom, CribroomAdmin)
admin.site.register(CribroomUser, CribroomUserAdmin)

admin.site.register(Desinfection, DesinfectionAdmin)
admin.site.register(Form, FormAdmin)

admin.site.register(Child, ChildAdmin)
admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Phone, PhoneAdmin)

admin.site.register(Shift, ShiftAdmin)

admin.site.register(Co_management, Co_managementAdmin)
admin.site.register(Sectional, SectionalAdmin)
admin.site.register(IdentType, IdentTypeAdmin)

admin.site.register(Neighborhood, NeighborhoodAdmin)

admin.site.register(Gender, GenderAdmin)
admin.site.register(GuardianType, GuardianTypeAdmin)
admin.site.register(PhoneFeature, PhoneFeatureAdmin)

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Zone, ZoneAdmin)

admin.site.register(Poll, PollAdmin)
admin.site.register(ChildAnswer, ChildAnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.register(TechnicalReport, TechnicalReportAdmin)
