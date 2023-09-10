from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
    ChildAndGuardian_RelatedObjectsView,
    CribroomModelViewSet,
    GroupViewSet,
    LocalityListView,
    NeighborhoodListView,
    GenderListView,
    ShiftListView,
    PhoneFeatureListView,
    GuardianTypeListView,
    PayoutViewSet,
    UserViewSet,
    ZoneModelViewSet,
    TechnicalReportRetrieveAPIView,
    DepartmentModelViewSet,
    LocalityListCreateView,
    PhoneFeatureListCreateView,
    GuardianListCreateView,
)

router = routers.DefaultRouter()

router.register(r"child", ChildModelViewSet)
router.register(r"cribroom", CribroomModelViewSet)
router.register(r"payout", PayoutViewSet)
router.register(r"zone", ZoneModelViewSet)
router.register(r"user", UserViewSet)
router.register(r"department", DepartmentModelViewSet)

urlpatterns = router.urls + [
    path(
        "technical-report/<pk>/<str:initial_date>/<str:end_date>/",
        TechnicalReportRetrieveAPIView.as_view(),
    ),
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
        "ShiftListView/",
        ShiftListView.as_view(),
        name="ShiftListView",
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
    path("GroupViewSet/", GroupViewSet.as_view({"get": "list"}), name="GroupViewSet"),
    path('LocalityListCreateView/', LocalityListCreateView.as_view(), name='LocalityListCreateView'),
    path('PhoneFeatureListCreateView/', PhoneFeatureListCreateView.as_view(), name='PhoneFeatureListCreateView'),
    path('GuardianListCreateView/', GuardianListCreateView.as_view(), name='GuardianListCreateView'),
]
