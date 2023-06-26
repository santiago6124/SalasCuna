from django.urls import path
from .views import (
    ChildListCreateView,
    ChildRetrieveUpdateDestroyView,
    GenderListCreateView,
    GenderRetrieveUpdateDestroyView,
    CribroomListCreateView,
    CribroomRetrieveUpdateDestroyView,
    ShiftListCreateView,
    ShiftRetrieveUpdateDestroyView,
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
    GuardianListCreateView,
    GuardianRetrieveUpdateDestroyView,
    ChildStateListCreateView,
    ChildStateRetrieveUpdateDestroyView,
    AllObjectsView,
)

urlpatterns = [
    path('all-objects/', AllObjectsView.as_view(), name='all-objects'),

    path('child/', ChildListCreateView.as_view(), name='child-list-create'),
    path('child/<int:pk>/', ChildRetrieveUpdateDestroyView.as_view(), name='child-retrieve-update-destroy'),
    path('gender/', GenderListCreateView.as_view(), name='gender-list-create'),
    path('gender/<int:pk>/', GenderRetrieveUpdateDestroyView.as_view(), name='gender-retrieve-update-destroy'),
    path('cribroom/', CribroomListCreateView.as_view(), name='cribroom-list-create'),
    path('cribroom/<int:pk>/', CribroomRetrieveUpdateDestroyView.as_view(), name='cribroom-retrieve-update-destroy'),
    path('shift/', ShiftListCreateView.as_view(), name='shift-list-create'),
    path('shift/<int:pk>/', ShiftRetrieveUpdateDestroyView.as_view(), name='shift-retrieve-update-destroy'),
    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('guardian/', GuardianListCreateView.as_view(), name='guardian-list-create'),
    path('guardian/<int:pk>/', GuardianRetrieveUpdateDestroyView.as_view(), name='guardian-retrieve-update-destroy'),
    path('childstate/', ChildStateListCreateView.as_view(), name='childstate-list-create'),
    path('childstate/<int:pk>/', ChildStateRetrieveUpdateDestroyView.as_view(), name='childstate-retrieve-update-destroy'),
]

urlpatterns  = [
    path('', views.getRoutes, name ='routes'),
]