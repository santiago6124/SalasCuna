from django.contrib import admin

# Register your models here.

#from .models import *
#admin.site.register(Addresses)
#admin.site.register()

from django.apps import apps

all_models = apps.get_models()

for model in all_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass