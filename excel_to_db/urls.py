from django.urls import path
from .views import storage_method

urlpatterns = [
    path('', storage_method, name="data migrate"),
]