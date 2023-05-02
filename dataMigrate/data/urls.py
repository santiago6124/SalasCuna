from django.urls import path
from .views import migration

urlpatterns = [
    path('migrate-data', migration, name="data migrate"),
]
