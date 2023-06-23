from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Child, Gender, Cribroom, Shift, User, Guardian, ChildState
from .serializers import (
    ChildSerializer,
    GenderSerializer,
    CribroomSerializer,
    ShiftSerializer,
    UserSerializer,
    GuardianSerializer,
    ChildStateSerializer,
)


class ChildListCreateView(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ChildRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class GenderListCreateView(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class CribroomListCreateView(generics.ListCreateAPIView):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer


class CribroomRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer


class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class ShiftRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GuardianListCreateView(generics.ListCreateAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer


class GuardianRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer


class ChildStateListCreateView(generics.ListCreateAPIView):
    queryset = ChildState.objects.all()
    serializer_class = ChildStateSerializer


class ChildStateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildState.objects.all()
    serializer_class = ChildStateSerializer
