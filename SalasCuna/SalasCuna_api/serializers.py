from rest_framework import serializers

# from django.contrib.auth.models import User

from .models import Child, Locality, Neighborhood, Gender, Cribroom, Shift, Guardian, ChildState


# entity Child {
#     + PRIMARY_KEY(id)
#     --
#     first_name
#     last_name
#     dni
#     birthdate
#     street
#     house_number
#     registration_date
#     disenroll_date = default null
#     --
#     FOREIGN_KEY(Locality)
#     FOREIGN_KEY(Neighborhood)
#     FOREIGN_KEY(Gender)
#     FOREIGN_KEY(Cribroom)
#     FOREIGN_KEY(Shift)
#     social_worker = FOREIGN_KEY(User)
#     FOREIGN_KEY(Guardian)
#     FOREIGN_KEY(Child_state)
#     --
#     ()
# }


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
