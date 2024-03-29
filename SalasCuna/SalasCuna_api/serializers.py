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

    Co_management,
    Sectional,
    IdentType,
    Phone,
    CribroomUser,
    Poll,
    Question,
    Answer,
    ChildAnswer,
    TechnicalReport
)


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"
        extra_kwargs = {
        }

class DepthPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"
        depth = 1

    # history = serializers.SerializerMethodField()

    # def get_history(self, obj):
    #     model = obj.history.__dict__['model']
    #     fields = "__all__"
    #     serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
    #     serializer.is_valid()
    #     return serializer.data

    # def get_age(self, obj):
    #     return obj.age()

class CribroomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CribroomUser
        fields = "__all__"

        extra_kwargs = {
        }

class DepthCribroomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CribroomUser
        fields = "__all__"
        depth = 1

    # history = serializers.SerializerMethodField()

    # def get_history(self, obj):
    #     model = obj.history.__dict__['model']
    #     fields = "__all__"
    #     serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
    #     serializer.is_valid()
    #     return serializer.data


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class QuestionDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        depth = 1

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

class AnswerDepthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
        depth = 1

class ChildAnswerSerializer(serializers.ModelSerializer):

    valueCorrectType = serializers.SerializerMethodField()

    def get_valueCorrectType(self, obj):
        return obj.returnValueAsAnswerType()

    class Meta:
        model = ChildAnswer
        fields = "__all__"

class ChildAnswerDepthSerializer(serializers.ModelSerializer):

    valueCorrectType = serializers.SerializerMethodField()

    def get_valueCorrectType(self, obj):
        return obj.returnValueAsAnswerType()

    class Meta:
        model = ChildAnswer
        fields = "__all__"
        depth = 1


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = "__all__"
        
        
class IdentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentType
        fields = "__all__"
        
        
class SectionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectional
        fields = "__all__"
        
        
class Co_managementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Co_management
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
            "house_number": {"required": False},
            "locality": {"required": False},
            "shift": {"required": False},
            "co_management": {"required": False},
        }

class DepthCribroomSerializer(serializers.ModelSerializer):
    lastDesinfection = DesinfectionSerializer(read_only=True)
    actualCapacity = serializers.SerializerMethodField()
    reachMax = serializers.SerializerMethodField()

    class Meta:
        model = Cribroom
        fields = "__all__"
        depth = 1

    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = "__all__"
        serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


    def get_actualCapacity(self, obj):
        return obj.actualCapacity()

    def get_pays(self, obj):
        return obj.totalImport()

    def get_reachMax(self, obj):
        return obj.reachMax()

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

        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "indentification": {"required": False},
            "ident_type": {"required": False},
        }

class DepthGuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        depth = 1
        fields = "__all__"

    # history = serializers.SerializerMethodField()

    # def get_history(self, obj):
    #     model = obj.history.__dict__['model']
    #     fields = "__all__"
    #     serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
    #     serializer.is_valid()
    #     return serializer.data


class PhoneFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneFeature
        fields = "__all__"


class GuardianTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianType
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = "__all__"
        
        extra_kwargs = {
            "first_name": {"required": False},
            "last_name": {"required": False},
            "indentification": {"required": False},
            "ident_type": {"required": False},
            "birthdate": {"required": False},
            "street": {"required": False},
            "house_number": {"required": False},
            "geolocation": {"required": False},
            "registration_date": {"required": False},
            "disenroll_date": {"required": False},
            "is_active": {"required": False},
            "locality": {"required": False},
            "neighborhood": {"required": False},
            "gender": {"required": False},
            "cribroom": {"required": False},
            "shift": {"required": False},
            "guardian": {"required": False},
        }
        

class DepthChildSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Child
        fields = "__all__"
        depth = 1

    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = "__all__"
        serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
        serializer.is_valid()
        return serializer.data

    def get_age(self, obj):
        return obj.age()


class TechnicalReportSerializer(serializers.ModelSerializer):
    pays = serializers.SerializerMethodField()
    maxCapacityStr = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()

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
    
    def get_department(self, obj):
        return obj.get_department()


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
    history = serializers.SerializerMethodField()

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = "__all__"
        serializer = HistoricalRecordSerializer(model, obj.history.all().order_by('history_date'), fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


    class Meta:
        model = UserAccount
        fields = "__all__"



class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        depth = 1
        fields = "__all__"



class TechnicalReportTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalReport
        exclude = ("id",)

class HistoricalRecordSerializer(serializers.ModelSerializer):
    def __init__(self, model, *args, fields='__all__', **kwargs):
        self.Meta.model = model
        self.Meta.fields = fields
        super().__init__()

    class Meta:
        pass
