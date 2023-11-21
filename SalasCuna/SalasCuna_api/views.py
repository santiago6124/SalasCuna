from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

# Custom permissions in permissions.py
from .permissions import (
    AllUsersPerms,
    AdministradorPerms,
    ArquitectoPerms,
    CoordinadorTSPerms,
    DevPerms,
    DirectorPerms,
    PsicopedagogaPerms,
    SecretarioPerms,
    TrabajadorSocialPerms,
)

from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from .models import (
    Child,
    Co_management,
    IdentType,
    Locality,
    Neighborhood,
    Gender,
    Cribroom,
    Sectional,
    Shift,
    Guardian,
    PhoneFeature,
    GuardianType,
    Payout,
    Zone,
    UserAccount,
    Department,
    Phone,
    CribroomUser,
)
from .serializers import (
    ChildSerializer,
    Co_managementSerializer,
    GroupSerializer,
    GuardianSerializer,
    DepthGuardianSerializer,
    IdentTypeSerializer,
    NeighborhoodSerializer,
    CribroomSerializer,
    DepthChildSerializer,
    LocalitySerializer,
    GenderSerializer,
    SectionalSerializer,
    ShiftSerializer,
    PhoneFeatureSerializer,
    GuardianTypeSerializer,
    PayoutSerializer,
    ZoneSerializer,
    UserSerializer,
    DepthCribroomSerializer,
    TechnicalReportSerializer,
    DepartmentSerializer,
    LogEntrySerializer,
    PhoneSerializer,
    CribroomUserSerializer,
    DepthCribroomUserSerializer,
    DepthPhoneSerializer,
)

from datetime import datetime, date
from rest_framework.views import APIView  # Import APIView from rest_framework

class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    filter_backends = [DjangoFilterBackend]  # This makes django-filters works
    filterset_fields = ["id", "phone_name", "phone_number", "phone_Feature", "guardian"]  # fields to filter
    
    # Para usar Serializer, utilizar el filtro debajo
    def get_queryset(self):
        #cribroomUser/?depth=True
        #cribroomUser/1/?depth=True
        # '1' para True y '0' para False

        depth = str(self.request.query_params.get("depth"))
        if depth=='1':
            self.serializer_class = DepthPhoneSerializer

        return super().get_queryset()

class CribroomUserModelViewSet(viewsets.ModelViewSet):
    queryset = CribroomUser.objects.all()
    serializer_class = CribroomUserSerializer
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    filter_backends = [DjangoFilterBackend]  # This makes django-filters works
    filterset_fields = ["id", "cribroom", "user"]  # fields to filter
    
    # Para usar Serializer, utilizar el filtro debajo
    def get_queryset(self):
        #cribroomUser/?depth=True
        #cribroomUser/1/?depth=True
        # '1' para True y '0' para False

        depth = str(self.request.query_params.get("depth"))
        if depth=='1':
            self.serializer_class = DepthCribroomUserSerializer

        return super().get_queryset()

class LocalityListCreateView(generics.ListCreateAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = [AllUsersPerms]
    filter_backends = [DjangoFilterBackend]  # This makes django-filters works
    filterset_fields = ["id", "locality"]  # fields to filter

class PhoneFeatureListCreateView(generics.ListCreateAPIView):
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    queryset = PhoneFeature.objects.all()
    serializer_class = PhoneFeatureSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["feature"]  # fields to filter


class GuardianModelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllUsersPerms]
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["identification"]  # fields to filter

    # Para usar Serializer, utilizar el filtro debajo
    def get_queryset(self):
        #guardian/?depth=True
        #guardian/1/?depth=True
        # '1' para True y '0' para False

        depth = str(self.request.query_params.get("depth"))
        if depth=='1':
            self.serializer_class = DepthGuardianSerializer

        return super().get_queryset()


class NeighborhoodListView(generics.ListAPIView):
    permission_classes = [AllUsersPerms]
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["neighborhood"]  # fields to filter


class GenderListView(generics.ListAPIView):
    permission_classes = [AllUsersPerms]
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["gender"]  # fields to filter


class PayoutViewSet(viewsets.ModelViewSet):
    permission_classes = [DevPerms | DirectorPerms]
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["amount", "zone_id"]  # fields to filter


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllUsersPerms]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        exclude_directora = self.request.query_params.get("exclude_directora")
        only_ts = self.request.query_params.get("only_ts")
        if exclude_directora is not None:
            self.queryset = Group.objects.exclude(name="Dev")
            self.queryset = self.queryset.exclude(name="Director")
        elif only_ts is not None:
            self.queryset = Group.objects.filter(name="Trabajador Social")

        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [DevPerms | DirectorPerms | IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer


class TechnicalReportRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [DevPerms | DirectorPerms | AdministradorPerms]
    queryset = Cribroom.objects.all()
    serializer_class = TechnicalReportSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["initial_date"] = self.kwargs.get("initial_date")
        context["end_date"] = self.kwargs.get("end_date")
        return context


class GuardianTypeListView(generics.ListAPIView):
    queryset = GuardianType.objects.all()
    serializer_class = GuardianTypeSerializer
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]


class ChildModelViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    filter_backends = [DjangoFilterBackend]  # This makes django-filters works
    filterset_fields = ["id", "locality", "cribroom_id"]  # fields to filter

    # Para usar Serializer, utilizar el filtro debajo
    def get_queryset(self):
        #child/?depth=True
        #child/1/?depth=True
        # '1' para True y '0' para False

        depth = str(self.request.query_params.get("depth"))
        if depth=='1':
            self.serializer_class = DepthChildSerializer

        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            updated_instance = serializer.save()
            if updated_instance.disenroll_date is not None:
                if updated_instance.disenroll_date <= date.today():
                    updated_instance.is_active = False
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CribroomListView(generics.ListAPIView):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = [
        "max_capacity",
        "is_active",
        "shift",
        "id",
    ]  # fields to filter

    def get_queryset(self):
        no_depth = self.request.query_params.get("no_depth")

        if no_depth is not None:
            self.queryset = Cribroom.objects.all()
            self.serializer_class = CribroomSerializer
            return super().get_queryset()
        else:
            self.queryset = Cribroom.objects.all()
            self.serializer_class = DepthCribroomSerializer
            return super().get_queryset()


class CribroomModelViewSet(viewsets.ModelViewSet):
    queryset = Cribroom.objects.all()
    serializer_class = CribroomSerializer
    permission_classes = [DevPerms | DirectorPerms]
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = [
        "max_capacity",
        "is_active",
        "shift",
        "id",
        'locality__department__zone__id'
    ]  # fields to filter

    def get_queryset(self):
        #cribroom/?depth=True
        #cribroom/1/?depth=True
        # '1' para True y '0' para False

        depth = str(self.request.query_params.get("depth"))
        if depth=='1':
            self.serializer_class = DepthCribroomSerializer

        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            updated_instance = serializer.save()
            if not updated_instance.is_active:
                children = Child.objects.all().filter(cribroom_id=instance.id)
                for child in children:
                    if child.is_active:
                        child.cribroom_isActive(False)
                        child.save()  # Guarda los cambios en la base de datos

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ShiftListCreateView(generics.ListCreateAPIView):
    permission_classes = [DevPerms | DirectorPerms | TrabajadorSocialPerms]
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["name"]  # fields to filter


class ZoneListCreateView(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [AllUsersPerms]
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]  # This makes django-filters works
    filterset_fields = ["name", 'id']  # fields to filter


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllUsersPerms]


class LogEntryModelViewSet(viewsets.ModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    permission_classes = [DevPerms | DirectorPerms]


class IdentTypeListView(generics.ListAPIView):
    permission_classes = [AllUsersPerms]
    queryset = IdentType.objects.all()
    serializer_class = IdentTypeSerializer
    
    
class SectionalListView(generics.ListAPIView):
    permission_classes = [AllUsersPerms]
    queryset = Sectional.objects.all()
    serializer_class = SectionalSerializer
    
    
class Co_managementListView(generics.ListAPIView):
    permission_classes = [AllUsersPerms]
    queryset = Co_management.objects.all()
    serializer_class = Co_managementSerializer