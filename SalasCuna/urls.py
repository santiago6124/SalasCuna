from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from django.conf import settings # new
from  django.conf.urls.static import static #new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("api/", include("SalasCuna_api.urls")),
    path('docs/', include_docs_urls(title='My API title', public=False)),
    re_path(r"^(?:.*)?$", TemplateView.as_view(template_name="index.html"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)