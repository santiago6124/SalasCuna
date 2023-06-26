from rest_framework import serializers
from .models import Child, Gender, Cribroom, Shift, User, Guardian, ChildState


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class CribroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cribroom
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'


class ChildStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildState
        fields = '__all__'


class ChildSerializer(serializers.ModelSerializer):
    gender = serializers.PrimaryKeyRelatedField(
        queryset=Gender.objects.all(),
        many=False,
        allow_null=True
    )
    cribroom = serializers.PrimaryKeyRelatedField(
        queryset=Cribroom.objects.all(),
        many=False,
        allow_null=True
    )
    shift = serializers.PrimaryKeyRelatedField(
        queryset=Shift.objects.all(),
        many=False,
        allow_null=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=False,
        allow_null=True
    )
    guardian = serializers.PrimaryKeyRelatedField(
        queryset=Guardian.objects.all(),
        many=False,
        allow_null=True
    )
    child_state = serializers.PrimaryKeyRelatedField(
        queryset=ChildState.objects.all(),
        many=False,
        allow_null=True
    )

    class Meta:
        model = Child
        fields = '__all__'
