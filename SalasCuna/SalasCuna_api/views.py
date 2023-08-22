from rest_framework import viewsets, status
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    DjangoModelPermissionsOrAnonReadOnly,
    AllowAny,
)
from rest_framework import mixins, generics, views
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import (
    Child,
    Locality,
    Neighborhood,
    Gender,
    Cribroom,
    Shift,
    Guardian,
    ChildState,
    PhoneFeature,
    GuardianType,
    Role,
    Payout,
    Zone,
    UserAccount,
)
from .serializers import (
    ChildSerializer,
    ChildAndGuardian_RelatedObjectsSerializer,
    GuardianSerializer,
    NeighborhoodSerializer,
    CribroomSerializer,
    DepthChildSerializer,
    RoleSerializer,
    LocalitySerializer,
    GenderSerializer,
    ShiftSerializer,
    PhoneFeatureSerializer,
    GuardianTypeSerializer,
    ChildStateSerializer,
    PayoutSerializer,
    ZoneSerializer,
    UserSerializer,
    DepthCribroomSerializer,
    TechnicalReportSerializer,
)

from datetime import datetime
from rest_framework.views import APIView  # Import APIView from rest_framework


class PayoutViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["amount", "zone"]  # fields to filter


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def get_queryset(self):
        exclude_directora = self.request.query_params.get("exclude_directora")

        if exclude_directora != None:
            self.queryset = Role.objects.exclude(name="Directora")

        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer


class ChildAndGuardian_RelatedObjectsView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        localitys = Locality.objects.all()
        neighborhoods = Neighborhood.objects.all()
        genders = Gender.objects.all()
        cribrooms = Cribroom.objects.all()
        shifts = Shift.objects.all()
        guardians = Guardian.objects.all()
        child_states = ChildState.objects.all()
        phone_Features = PhoneFeature.objects.all()
        guardian_Types = GuardianType.objects.all()

        serializer = ChildAndGuardian_RelatedObjectsSerializer(
            {
                "locality": localitys,
                "neighborhood": neighborhoods,
                "gender": genders,
                "cribroom": cribrooms,
                "shift": shifts,
                "guardian": guardians,
                "child_state": child_states,
                "phone_Feature": phone_Features,
                "guardian_Type": guardian_Types,
            }
        )

        return Response(serializer.data)

class TechnicalReportRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Cribroom.objects.all()
    serializer_class = TechnicalReportSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['initial_date'] = self.kwargs.get('initial_date')
        context['end_date'] = self.kwargs.get('end_date')
        return context
    

class LocalityListView(generics.ListAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = [AllowAny]


class NeighborhoodListView(generics.ListAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    permission_classes = [AllowAny]


class GenderListView(generics.ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [AllowAny]


class CribroomListView(generics.ListAPIView):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer
    permission_classes = [AllowAny]


class ShiftListView(generics.ListAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [AllowAny]


class ChildStateListView(generics.ListAPIView):
    queryset = ChildState.objects.all()
    serializer_class = ChildStateSerializer
    permission_classes = [AllowAny]


class PhoneFeatureListView(generics.ListAPIView):
    queryset = PhoneFeature.objects.all()
    serializer_class = PhoneFeatureSerializer
    permission_classes = [AllowAny]


class GuardianTypeListView(generics.ListAPIView):
    queryset = GuardianType.objects.all()
    serializer_class = GuardianTypeSerializer
    permission_classes = [AllowAny]


class ChildModelViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]  # This makes django-filters works
    filterset_fields = ["id", "locality", "cribroom_id"]  # fields to filter

    # Para usar Serializer, utilizar el filtro debajo
    def get_queryset(self):
        self.queryset = Child.objects.all()
        self.serializer_class = DepthChildSerializer

        return super().get_queryset()

    def perform_create(self, serializer):
        # First, create the Child object
        child_instance = serializer.save()

        request_data = self.request.data

        if child_instance.guardian is None:
            # Now, create the associated Guardian object
            guardian_data = {
                "first_name": request_data.get("guardian_first_name"),
                "last_name": request_data.get("guardian_last_name"),
                "dni": request_data.get("guardian_dni"),
                "phone_number": request_data.get("guardian_phone_number"),
                "phone_Feature": request_data.get("guardian_phone_Feature_id"),
                "guardian_Type": request_data.get("guardian_guardian_Type_id"),
                "gender": request_data.get("guardian_gender_id"),
            }

            guardian_serializer = GuardianSerializer(data=guardian_data)
            if guardian_serializer.is_valid():
                guardian_instance = guardian_serializer.save()
                child_instance.guardian = guardian_instance
                child_instance.save()
            else:
                # If the guardian serializer is not valid, you may handle the error here
                print(guardian_serializer.errors)

                return Response(
                    {"message": "check the guardian data"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if (
            child_instance.neighborhood is None
            and request_data.get("neighborhood_neighborhood") is None
        ):
            # Now, create the associated Neighborhood object
            neighborhood_data = {
                "neighborhood": request_data.get("neighborhood_neighborhood"),
            }

            neighborhood_serializer = NeighborhoodSerializer(data=neighborhood_data)
            if neighborhood_serializer.is_valid():
                neighborhood_instance = neighborhood_serializer.save()
                child_instance.neighborhood = neighborhood_instance
                child_instance.save()
            else:
                # If the Neighborhood serializer is not valid, you may handle the error here
                print(neighborhood_serializer.errors)

                return Response(
                    {"message": "check the neighborhood data"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        disenroll = bool(self.request.query_params.get("disenroll"))
        # disenroll_date
        print(f"paramter: {disenroll}")

        if disenroll == True:
            print(f"disenroll: {disenroll}")
            instance.disenroll_date = datetime.now()
            instance.child_state = ChildState.objects.get(name="Inactive")
            print(instance)
            print(ChildState.objects.get(name="Inactive"))
            # instance.user=self.request.user
            instance.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            # If 'disenroll' parameter is not present, proceed with normal update
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CribroomModelViewSet(viewsets.ModelViewSet):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = [
        "max_capacity",
        "is_active",
        "zone",
        "shift",
        "id",
    ]  # fields to filter

    def get_queryset(self):
        no_depth = self.request.query_params.get("no_depth")

        if no_depth != None:
            self.queryset = Cribroom.objects.all()
            self.serializer_class = CribroomSerializer
            return super().get_queryset()
        else:
            self.queryset = Cribroom.objects.all()
            self.serializer_class = DepthCribroomSerializer
            return super().get_queryset()


class ShiftModelViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    permission_classes = [AllowAny]


class ZoneModelViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [AllowAny]
