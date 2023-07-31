from rest_framework import serializers

# from django.contrib.auth.models import User

from .models import Child, Locality, Neighborhood, Gender, Cribroom, Shift, Guardian, ChildState



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

class ChildRelatedObjectsSerializer(serializers.Serializer):
    locality = LocalitySerializer(many=True)
    neighborhood = NeighborhoodSerializer(many=True)
    gender = GenderSerializer(many=True)
    cribroom = CribroomSerializer(many=True)
    shift = ShiftSerializer(many=True)
    guardian = GuardianSerializer(many=True)
    child_state = ChildStateSerializer(many=True)


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = "__all__"
        read_only_fields = ['user']
