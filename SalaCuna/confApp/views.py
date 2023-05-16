from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Children, Guardians, Addresses
from .serializers import ChildrenSerializer, GuardiansSerializer, AddressesSerializer

class ChildrenListCreateView(generics.ListCreateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

class ChildrenRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

class GuardiansListCreateView(generics.ListCreateAPIView):
    queryset = Guardians.objects.all()
    serializer_class = GuardiansSerializer

class AddressesListCreateView(generics.ListCreateAPIView):
    queryset = Addresses.objects.all()
    serializer_class = AddressesSerializer