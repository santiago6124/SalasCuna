from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
    CribroomModelViewSet,
    GroupViewSet,
    GuardianTypeListView,
    PayoutViewSet,
    UserViewSet,
    ZoneModelViewSet,
    TechnicalReportRetrieveAPIView,
    DepartmentModelViewSet,
    LocalityListCreateView,
    PhoneFeatureListCreateView,
    GuardianListCreateView,
    NeighborhoodListCreateView,
    GenderListCreateView,
    LogEntryModelViewSet,
    CribroomListView,
)

router = routers.DefaultRouter()

router.register(r"child", ChildModelViewSet)
router.register(r"cribroomDir", CribroomModelViewSet)
router.register(r"payout", PayoutViewSet)
router.register(r"zone", ZoneModelViewSet)
router.register(r"user", UserViewSet)
router.register(r"department", DepartmentModelViewSet)
router.register(r"logEntry", LogEntryModelViewSet)

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
        "GuardianListCreateView/",
        GuardianListCreateView.as_view(),
        name="GuardianListCreateView",
    ),
    path(
        "NeighborhoodListCreateView/",
        NeighborhoodListCreateView.as_view(),
        name="NeighborhoodListCreateView",
    ),
    path(
        "GenderListCreateView/",
        GenderListCreateView.as_view(),
        name="GenderListCreateView",
    ),
]
