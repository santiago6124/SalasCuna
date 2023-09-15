from rest_framework import serializers

# from django.contrib.auth.models import User

from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from .models import (
    Child,
    Locality,
    Neighborhood,
    Gender,
    Cribroom,
    Shift,
    Guardian,
    PhoneFeature,
    GuardianType,
    Payout,
    Zone,
    UserAccount,
    Desinfection,
    Department,
    Poll,
    Question,
    Answer,
    ChildAnswer,
)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class ChildAnswerSerializer(serializers.ModelSerializer):

    valueCorrectType = serializers.SerializerMethodField()

    def get_valueCorrectType(self, obj):
        return obj.returnValueAsAnswerType()

    class Meta:
        model = ChildAnswer
        fields = "__all__"


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class DesinfectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desinfection
        fields = ["date"]


class CribroomSerializer(serializers.ModelSerializer):
    lastDesinfection = DesinfectionSerializer(read_only=True)
    actualCapacity = serializers.SerializerMethodField()
    reachMax = serializers.SerializerMethodField()

    def get_actualCapacity(self, obj):
        return obj.actualCapacity()

    def get_pays(self, obj):
        return obj.totalImport()

    def get_reachMax(self, obj):
        return obj.reachMax()

    class Meta:
        model = Cribroom
        fields = "__all__"

    """
    ESTO ES PARA HACER DISPLAY DEL DICCIONARIO CON EL HISTORIAL/AUDITORIA
    RETURN HISTORIAL: list[dictionary{attribute: value, attribute: value}, dictionary{attribute: value, attribute: value}]
    
    history = serializers.SerializerMethodField()
    

    def get_history(self, instance):
        return instance.history.values()
    
    """


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"


class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = "__all__"


class PhoneFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneFeature
        fields = "__all__"


class GuardianTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianType
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Child
        fields = "__all__"
        read_only_fields = ["user"]

    def get_age(self, obj):
        return obj.age()


class DepthGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        depth = 1
        fields = "__all__"


class DepthCribroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cribroom
        depth = 1
        fields = "__all__"


class TechnicalReportSerializer(serializers.ModelSerializer):
    pays = serializers.SerializerMethodField()
    maxCapacityStr = serializers.SerializerMethodField()

    class Meta:
        model = Cribroom
        depth = 1
        fields = "__all__"

    def get_pays(self, obj):
        initial_date = self.context.get("initial_date")
        end_date = self.context.get("end_date")
        return obj.totalImport(initial_date, end_date)

    def get_maxCapacityStr(self, obj):
        return obj.maxCapacityStr()


class DepthChildSerializer(serializers.ModelSerializer):
    guardian = DepthGuardianSerializer()

    class Meta:
        model = Child
        fields = "__all__"
        depth = 1
        read_only_fields = ["user"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"


class DeleteCribroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cribroom
        fields = "__all__"
        extra_kwargs = {
            "name": {"required": False},
            "entity": {"required": False},
            "CUIT": {"required": False},
            "code": {"required": False},
            "max_capacity": {"required": False},
            "street": {"required": False},
        }


class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        depth = 1
        fields = "__all__"
