from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
    ChildAndGuardian_RelatedObjectsView,
    CribroomModelViewSet,
    RoleViewSet,
    LocalityListView,
    NeighborhoodListView,
    GenderListView,
    CribroomListView,
    ShiftListView,
    ChildStateListView,
    PhoneFeatureListView,
    GuardianTypeListView,
    PayoutViewSet,
    ZoneReadOnlyModelViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()

router.register(r"child", ChildModelViewSet)
router.register(r"cribroom", CribroomModelViewSet)
router.register(r"payout", PayoutViewSet)
router.register(r"zone", ZoneReadOnlyModelViewSet)
router.register(r"user", UserViewSet)

urlpatterns = router.urls + [
    path(
        "ChildRelatedObjectsView/",
        ChildAndGuardian_RelatedObjectsView.as_view(),
        name="ChildRelatedObjectsView",
    ),
    path(
        "LocalityListView/",
        LocalityListView.as_view(),
        name="LocalityListView",
    ),
    path(
        "NeighborhoodListView/",
        NeighborhoodListView.as_view(),
        name="NeighborhoodListView",
    ),
    path(
        "GenderListView/",
        GenderListView.as_view(),
        name="GenderListView",
    ),
    path(
        "CribroomListView/",
        CribroomListView.as_view(),
        name="CribroomListView",
    ),
    path(
        "ShiftListView/",
        ShiftListView.as_view(),
        name="ShiftListView",
    ),
    path(
        "ChildStateListView/",
        ChildStateListView.as_view(),
        name="ChildStateListView",
    ),
    path(
        "PhoneFeatureListView/",
        PhoneFeatureListView.as_view(),
        name="PhoneFeatureListView",
    ),
    path(
        "GuardianTypeListView/",
        GuardianTypeListView.as_view(),
        name="GuardianTypeListView",
    ),
    path("RoleViewSet/", RoleViewSet.as_view({"get": "list"}), name="RoleViewSet"),
]
