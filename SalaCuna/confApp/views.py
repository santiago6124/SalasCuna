from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status

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
    AllObjectsSerializer,
)


class ChildListCreateView(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    
    permission_classes = []

    def get_serializer(self, *args, **kwargs):
        # Use modified serializer for POST requests
        if self.request.method == 'POST':
            serializer_class = self.get_serializer_class()
            kwargs['context'] = self.get_serializer_context()
            return serializer_class(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)


class AllObjectsView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        genders = Gender.objects.all()
        cribrooms = Cribroom.objects.all()
        shifts = Shift.objects.all()
        users = User.objects.all()
        guardians = Guardian.objects.all()
        child_states = ChildState.objects.all()
        childs = Child.objects.all()

        serializer = AllObjectsSerializer({
            'genders': genders,
            'cribrooms': cribrooms,
            'shifts': shifts,
            'users': users,
            'guardians': guardians,
            'child_states': child_states,
            'childs': childs
        })
        return Response(serializer.data)


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
