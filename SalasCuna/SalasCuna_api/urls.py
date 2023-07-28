from django.urls import include, path
from rest_framework import routers
from .views import ChildModelViewSet, ChildRelatedObjectsView

router = routers.DefaultRouter()

router.register(r'child', ChildModelViewSet)

urlpatterns =  router.urls + [
    path('ChildRelatedObjectsView/', ChildRelatedObjectsView.as_view(), name='ChildRelatedObjectsView'),
]