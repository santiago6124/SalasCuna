from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework import mixins, generics, views
from rest_framework.response import Response

from .models import Child, Locality, Neighborhood, Gender, Cribroom, Shift, Guardian, ChildState
from .serializers import ChildSerializer, ChildRelatedObjectsSerializer

from datetime import datetime

class ChildRelatedObjectsView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        localitys = Locality.objects.all()
        neighborhoods = Neighborhood.objects.all()
        genders = Gender.objects.all()
        cribrooms = Cribroom.objects.all()
        shifts = Shift.objects.all()
        guardians = Guardian.objects.all()
        child_states = ChildState.objects.all()

        serializer = ChildRelatedObjectsSerializer({
            'locality' : localitys,
            'neighborhood' : neighborhoods,
            'gender': genders,
            'cribroom': cribrooms,
            'shift': shifts,
            'guardian': guardians,
            'child_state': child_states,
        })

        return Response(serializer.data)

class ChildModelViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [AllowAny]
