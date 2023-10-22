from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/", include("SalasCuna_api.urls")),
    path('docs/', include_docs_urls(title='My API title', public=False)),
    re_path(r"^(?:.*)?$", TemplateView.as_view(template_name="index.html"))
]