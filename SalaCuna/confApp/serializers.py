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
    gender = GenderSerializer()
    cribroom = CribroomSerializer()
    shift = ShiftSerializer()
    user = UserSerializer()
    guardian = GuardianSerializer()
    child_state = ChildStateSerializer()

    class Meta:
        model = Child
        fields = '__all__'
