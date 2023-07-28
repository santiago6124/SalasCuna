from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Adress)
admin.site.register(Child)
admin.site.register(ChildState)
admin.site.register(Company)
admin.site.register(Cribroom)
admin.site.register(CribroomUser)
admin.site.register(Desinfection)
admin.site.register(Form)
admin.site.register(Gender)
admin.site.register(Locality)
admin.site.register(Neighborhood)
admin.site.register(PhoneFeature)
admin.site.register(GuardianType)
admin.site.register(Guardian)
admin.site.register(Payout)
admin.site.register(Role)
admin.site.register(Shift)
admin.site.register(UserEmail)
admin.site.register(User)
admin.site.register(UserAccount)
admin.site.register(Zone)
