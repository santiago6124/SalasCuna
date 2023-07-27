from django.urls import path
from .views import migration

urlpatterns = [
    path('', migration, name="data migrate"),
]