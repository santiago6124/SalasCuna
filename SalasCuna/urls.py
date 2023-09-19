from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/", include("SalasCuna_api.urls")),
    #path("excel-to-db/", include("excel_to_db.urls")),
    re_path(r"^(?:.*)?$", TemplateView.as_view(template_name="index.html"))
]
