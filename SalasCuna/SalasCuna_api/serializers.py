from rest_framework import serializers, viewsets

# from django.contrib.auth.models import User

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
    UserAccount,
)


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = "__all__"


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class CribroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cribroom
        depth = 1
        fields = "__all__"


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = "__all__"


class ChildStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildState
        fields = "__all__"


class PhoneFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneFeature
        fields = "__all__"


class GuardianTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianType
        fields = "__all__"


class ChildAndGuardian_RelatedObjectsSerializer(serializers.Serializer):
    locality = LocalitySerializer(many=True)
    neighborhood = NeighborhoodSerializer(many=True)
    gender = GenderSerializer(many=True)
    cribroom = CribroomSerializer(many=True)
    shift = ShiftSerializer(many=True)
    guardian = GuardianSerializer(many=True)
    child_state = ChildStateSerializer(many=True)
    phone_Feature = PhoneFeatureSerializer(many=True)
    guardian_Type = GuardianTypeSerializer(many=True)


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
        read_only_fields = ["user"]


class DepthGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        depth = 1
        fields = "__all__"


class DepthChildSerializer(serializers.ModelSerializer):
    guardian = DepthGuardianSerializer()

    class Meta:
        model = Child
        depth = 1
        fields = "__all__"
        read_only_fields = ["user"]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["first_name", "last_name", "email", "role", "phone_number", "dni"]
