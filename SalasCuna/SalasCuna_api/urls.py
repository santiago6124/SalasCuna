from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
    Co_managmentListView,
    CribroomModelViewSet,
    GroupViewSet,
    GuardianTypeListView,
    IdentTypeListView,
    PayoutViewSet,
    SectionalListView,
    UserViewSet,
    ZoneListCreateView,
    TechnicalReportRetrieveAPIView,
    DepartmentListCreateView,
    LocalityListCreateView,
    PhoneFeatureListCreateView,
    GuardianModelViewSet,
    NeighborhoodListView,
    GenderListView,
    LogEntryModelViewSet,
    CribroomListView,
    ShiftListCreateView,
)

router = routers.DefaultRouter()

router.register(r"child", ChildModelViewSet)
router.register(r"cribroomDir", CribroomModelViewSet)
router.register(r"payout", PayoutViewSet)
router.register(r"user", UserViewSet)
router.register(r"logEntry", LogEntryModelViewSet)
router.register(r"GuardianListCreateView", GuardianModelViewSet)

urlpatterns = router.urls + [
    path(
        "technical-report/<pk>/<str:initial_date>/<str:end_date>/",
        TechnicalReportRetrieveAPIView.as_view(),
    ),
    path(
        "GuardianTypeListView/",
        GuardianTypeListView.as_view(),
        name="GuardianTypeListView",
    ),
    path("GroupViewSet/", GroupViewSet.as_view({"get": "list"}), name="GroupViewSet"),
    path("cribroom/", CribroomListView.as_view(), name="cribroom"),
    path(
        "LocalityListCreateView/",
        LocalityListCreateView.as_view(),
        name="LocalityListCreateView",
    ),
    path(
        "PhoneFeatureListCreateView/",
        PhoneFeatureListCreateView.as_view(),
        name="PhoneFeatureListCreateView",
    ),
    path(
        "NeighborhoodListCreateView/",
        NeighborhoodListView.as_view(),
        name="NeighborhoodListCreateView",
    ),
    path(
        "GenderListCreateView/",
        GenderListView.as_view(),
        name="GenderListCreateView",
    ),
    path(
        "IdentTypeListCreateView/",
        IdentTypeListView.as_view(),
        name="IdentTypeListCreateView",
    ),
    path(
        "SectionalListCreateView/",
        SectionalListView.as_view(),
        name="SectionalListCreateView",
    ),
    path(
        "Co_managmentListCreateView/",
        Co_managmentListView.as_view(),
        name="Co_managmentListCreateView",
    ),
    path(
        "shift/",
        ShiftListCreateView.as_view(),
        name="ShiftListCreateView",
    ),
    path(
        "department/",
        DepartmentListCreateView.as_view(),
        name="DepartmentListCreateView",
    ),
    path(
        "zone/",
        ZoneListCreateView.as_view(),
        name="ZoneListCreateView",
    ),
]
