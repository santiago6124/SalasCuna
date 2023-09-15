from django.urls import include, path
from rest_framework import routers
from .views import (
    ChildModelViewSet,
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
    NeighborhoodListCreateView,
    GenderListCreateView,
    ShiftListCreateView,
    ChildListCreateView,
    LogEntryModelViewSet,
    CribroomListView,
    PollListView,
    QuestionListView,
    AnswerListView,
    ChildAnswerListCreateView,
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
    path(
        "ShiftListCreateView/",
        ShiftListCreateView.as_view(),
        name="ShiftListCreateView",
    ),
    path(
        "ChildListCreateView/",
        ChildListCreateView.as_view(),
        name="ChildListCreateView",
    ),
    path(
        "PollListView/",
        PollListView.as_view(),
        name="PollListView",
    ),
    path(
        "QuestionListView/",
        QuestionListView.as_view(),
        name="QuestionListView",
    ),
    path(
        "AnswerListView/",
        AnswerListView.as_view(),
        name="AnswerListView",
    ),
    path(
        "ChildAnswerListCreateView/",
        ChildAnswerListCreateView.as_view(),
        name="ChildAnswerListCreateView",
    ),
]
