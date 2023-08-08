from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
    ChildAndGuardian_RelatedObjectsView,
    CribroomModelViewSet,
    RoleViewSet,
    ShiftModelViewSet,
    ZoneModelViewSet
)

router = routers.DefaultRouter()

router.register(r"child", ChildModelViewSet)
router.register(r"cribroom", CribroomModelViewSet)
router.register(r"shift", ShiftModelViewSet)
router.register(r"zone", ZoneModelViewSet)

urlpatterns = router.urls + [
    path(
        "ChildRelatedObjectsView/",
        ChildAndGuardian_RelatedObjectsView.as_view(),
        name="ChildRelatedObjectsView",
    ),
    path("RoleViewSet/", RoleViewSet.as_view({"get": "list"}), name="RoleViewSet"),
]
