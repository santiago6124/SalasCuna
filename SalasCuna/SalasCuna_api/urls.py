from django.urls import include, path
from rest_framework import routers
from .views import ChildModelViewSet, ChildAndGuardian_RelatedObjectsView, CribroomModelViewSet

router = routers.DefaultRouter()

router.register(r'child', ChildModelViewSet)
router.register(r'cribroom', CribroomModelViewSet)

urlpatterns =  router.urls + [
    path('ChildRelatedObjectsView/', ChildAndGuardian_RelatedObjectsView.as_view(), name='ChildRelatedObjectsView'),
]