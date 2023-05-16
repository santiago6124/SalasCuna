from django.urls import path
from .views import ChildrenListCreateView, ChildrenRetrieveUpdateDestroyView, AddressesListCreateView, GuardiansListCreateView

urlpatterns = [
    path('children/', ChildrenListCreateView.as_view(), name='children-list-create'),
    path('children/<int:pk>/', ChildrenRetrieveUpdateDestroyView.as_view(), name='children-retrieve-update-destroy'),
    path('addresses/', AddressesListCreateView.as_view(), name='addresses-list-create'),
    path('guardians/', GuardiansListCreateView.as_view(), name='guardians-list-create'),
]
