from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Addresses)
admin.site.register(Answers)
admin.site.register(Children)
admin.site.register(ChildrenState)
admin.site.register(Cribrooms)
admin.site.register(Departments)
admin.site.register(Desinfections)
admin.site.register(Districts)
admin.site.register(Forms)
admin.site.register(Genders)
admin.site.register(GuardianPhones)
admin.site.register(Guardians)
admin.site.register(Localities)
admin.site.register(Options)
admin.site.register(Padrones)
admin.site.register(Paynote)
admin.site.register(Payouts)
admin.site.register(QuestionTypes)
admin.site.register(Questions)
admin.site.register(Roles)
admin.site.register(Shifts)
admin.site.register(UserEmails)
admin.site.register(Users)
admin.site.register(Zones)
