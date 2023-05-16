from rest_framework import serializers
from .models import Children, Guardians, Addresses

class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields = '__all__'


class GuardiansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardians
        fields = '__all__'

class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
