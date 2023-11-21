# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from datetime import date
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from simple_history.models import HistoricalRecords
from num2words import num2words

from django.core.exceptions import ValidationError


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        extra_fields.setdefault("is_active", True)

        
        user.set_password(password)
        user.save()
        

        return user  # Add this line to return the created user object

    def create_superuser(self, email, password=None, **extra_fields):
        # extra_fields.setdefault("is_staff", True)
        # extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault(
            "is_active", True
        )  # Make sure to set is_active to True for superusers
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dni = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(
        "Department",
        on_delete=models.CASCADE,
        db_column="Department_id",
        blank=True,
        null=True,
    )
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    history = HistoricalRecords()

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "dni", "phone_number", "address", "city", "department"]

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.email}, ({self.last_name}, {self.first_name})"


class Department(models.Model):
    department = models.CharField(max_length=255, blank=False)

    zone = models.ForeignKey(
        "Zone", on_delete=models.CASCADE, blank=False
    )

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.department}"

class Locality(models.Model):
    locality = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return f"{self.locality}"

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.neighborhood}"

class Sectional(models.Model):
    sectional = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.sectional}"

class Co_management(models.Model):
    co_management = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.co_management}"

class IdentType(models.Model):
    type = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return self.type


class Child(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    identification = models.CharField(max_length=255, blank=True, null=True)
    ident_type = models.ForeignKey(
        "IdentType", on_delete=models.CASCADE, blank=False
    )
    birthdate = models.DateField(blank=False)
    street = models.CharField(max_length=255, blank=False)
    house_number = models.IntegerField(blank=False, null=False )
    geolocation = models.CharField(max_length=255, blank=True, null=True)
    
    registration_date = models.DateField(blank=False)
    disenroll_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, default=True)

    locality = models.ForeignKey(
        "Locality", on_delete=models.CASCADE, blank=False, null=False
    )
    neighborhood = models.ForeignKey(
        "Neighborhood", on_delete=models.CASCADE, blank=False, null=False
    )
    gender = models.ForeignKey(
        "Gender", models.DO_NOTHING, db_column="Gender_id", blank=False, null=False
    )  # Field name made lowercase.
    cribroom = models.ForeignKey(
        "Cribroom", models.DO_NOTHING, db_column="Cribroom_id", blank=False, null=False
    )  # Field name made lowercase.
    shift = models.ForeignKey(
        "Shift", models.DO_NOTHING, db_column="Shift_id", blank=False, null=False
    )  # Field name made lowercase.

    guardian = models.ForeignKey(
        "Guardian", models.DO_NOTHING, db_column="Guardian_id", blank=False, null=False
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def cribroom_isActive(self, param):
        if not param:
            self.is_active = False
            self.save()

    def age(self):
        today = date.today()
        birthdate = self.birthdate
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        return age


class Company(models.Model):
    title = models.CharField(max_length=255, blank=False)
    phone = models.IntegerField(blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return self.title


class Cribroom(models.Model):
    name = models.CharField(max_length=255, blank=False)
    entity = models.CharField(max_length=255, blank=False)
    CUIT = models.BigIntegerField(blank=False)  # nuevos campos
    code = models.CharField(max_length=255, blank=False)
    max_capacity = models.IntegerField(blank=False)
    is_active = models.BooleanField(default=True)
    street = models.CharField(max_length=255, blank=False)
    house_number = models.IntegerField(blank=False, null=False)
    geolocation = models.CharField(max_length=255, blank=False, null=True)

    locality = models.ForeignKey(
        Locality, on_delete=models.CASCADE
    )
    shift = models.ForeignKey(
        "Shift", models.DO_NOTHING, db_column="Shift_id"
    )  # Field name made lowercase.
    
    co_management = models.ForeignKey(
        "Co_management", models.DO_NOTHING, db_column="Co_management_id"
    )  # Field name made lowercase.


    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=False, null=True
    )
    sectional = models.ForeignKey(
        "Sectional", models.DO_NOTHING, db_column="Sectional_id", blank=False, null=True
    )  # Field name made lowercase.
    
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name}, COD: {self.code}, CUIT: {self.CUIT}"

    def lastDesinfection(self):
        # Utiliza el atributo ForeignKey 'desinfection_set' para acceder a las desinfecciones asociadas
        # a esta cribroom, y ordena los resultados por la fecha en orden descendente para obtener la última.
        lastDesinfection = self.desinfection_set.order_by("-date").first()
        return lastDesinfection

    def actualCapacity(self):
        return self.child_set.filter(is_active=True).count()

    def reachMax(self):
        if self.actualCapacity() == self.max_capacity:
            return True
        else:
            return False
        
    def get_department(self):
        return self.locality.department.department
    

    def totalImport(self, init_date, end_date):
        """
        calcular en base a maximo de chico x valor por mes durante los siguientes 12 meses

        for n in 12_months:
            month_import_n = max_capacity * amount
            
        calculando proporcionalmente el month_import_0 y el month_import_-1
            segun la cantidad de dias seleccionados. Formula:
            initYear, initMonth, initDay = 2022, 2, 11 
            initAmount  = 15006.0
            init_days_in_month = calendar.monthrange(initYear, initMonth)[1]

            initAmountProporcional = (initAmount/init_days_in_month) * (init_days_in_month - initDay)
            endAmountProporcional = (endAmount/end_days_in_month) * (0 + initDay)
            
        """
        try:
            payouts = Payout.objects.filter(
                zone=self.locality.department.zone.id, date__range=[init_date, end_date]
            )
            print(f"payouts: {payouts}")
            min_date = min(payouts, key=lambda payout: payout.date).date
            max_date = max(payouts, key=lambda payout: payout.date).date

            pays = {}

            pays["totalSumEndMonth"] = max_date.month
            pays["totalSumEndYear"] = max_date.year
            pays["totalSumInitMonth"] = min_date.month
            pays["totalSumInitYear"] = min_date.year

            for payout in payouts:
                pays[str(payout.date)] = payout.amount * self.max_capacity

                try:
                    pays[str(payout.date.year)] += payout.amount * self.max_capacity
                except:
                    pays[str(payout.date.year)] = payout.amount * self.max_capacity

                try:
                    pays["totalSumFloat"] += payout.amount * self.max_capacity
                    pays["totalSumStr"] = num2words(pays["totalSumFloat"], lang="es")
                except:
                    pays["totalSumFloat"] = payout.amount * self.max_capacity
                    pays["totalSumStr"] = num2words(pays["totalSumFloat"], lang="es")

                try:
                    pays["firstSubTotalSumFloat"] += (
                        payout.amount * self.max_capacity
                        if payout.date.year <= pays["totalSumInitYear"]
                        else 0
                    )

                except:
                    pays["firstSubTotalSumFloat"] = (
                        payout.amount * self.max_capacity
                        if payout.date.year <= pays["totalSumInitYear"]
                        else 0
                    )

                try:
                    pays["SecSubTotalSumFloat"] += (
                        payout.amount * self.max_capacity
                        if payout.date.year >= pays["totalSumEndYear"]
                        else 0
                    )
                except:
                    pays["SecSubTotalSumFloat"] = (
                        payout.amount * self.max_capacity
                        if payout.date.year >= pays["totalSumEndYear"]
                        else 0
                    )

                try:
                    pays["firstSubTotalSumEndMonth"] = (
                        payout.date.month
                        if payout.date.year <= pays["totalSumInitYear"]
                        and payout.date.month >= pays["firstSubTotalSumEndMonth"]
                        else pays["firstSubTotalSumEndMonth"]
                    )
                except:
                    pays["firstSubTotalSumEndMonth"] = (
                        payout.date.month
                        if payout.date.year <= pays["totalSumInitYear"]
                        else 100
                    )

                try:
                    pays["SecSubTotalSumInitMonth"] = (
                        payout.date.month
                        if payout.date.year >= pays["totalSumEndYear"]
                        and payout.date.month <= pays["SecSubTotalSumInitMonth"]
                        else pays["SecSubTotalSumInitMonth"]
                    )
                except:
                    pays["SecSubTotalSumInitMonth"] = (
                        payout.date.month
                        if payout.date.year >= pays["totalSumEndYear"]
                        else 100
                    )

            month_names_spanish = {
                1: "enero",
                2: "febrero",
                3: "marzo",
                4: "abril",
                5: "mayo",
                6: "junio",
                7: "julio",
                8: "agosto",
                9: "septiembre",
                10: "octubre",
                11: "noviembre",
                12: "diciembre",
            }

            pays["totalSumEndMonth"] = month_names_spanish[pays["totalSumEndMonth"]]
            pays["totalSumInitMonth"] = month_names_spanish[pays["totalSumInitMonth"]]
            pays["firstSubTotalSumEndMonth"] = month_names_spanish[
                pays["firstSubTotalSumEndMonth"]
            ]
            pays["SecSubTotalSumInitMonth"] = month_names_spanish[
                pays["SecSubTotalSumInitMonth"]
            ]

        except Exception as e:
            return f"An error ocurred: {e}"

        return pays

    def maxCapacityStr(self):
        return num2words(self.max_capacity, lang="es")


class CribroomUser(models.Model):
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=False
    )  # Field name made lowercase.
    user = models.ForeignKey(
        "UserAccount", models.DO_NOTHING, db_column="User_id", blank=False
    )  # Field name made lowercase.

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user}, {self.cribroom}"


class Desinfection(models.Model):
    date = models.DateTimeField(blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=False
    )  # Field name made lowercase.
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column="Company_id", blank=False
    )  # Field name made lowercase.

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.cribroom}, {self.date}"


class Form(models.Model):
    generation_date = models.DateField(blank=False)
    cribroom_user = models.ForeignKey(
        CribroomUser, models.DO_NOTHING, db_column="Cribroom_User_id", blank=False
    )  # Field name made lowercase.

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}, {self.generation_date}"


class Gender(models.Model):
    gender = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.gender}"


class PhoneFeature(models.Model):
    feature = models.BigIntegerField(blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.feature}"


class GuardianType(models.Model):
    type = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.type}"

class Guardian(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    identification = models.CharField(max_length=255, blank=False, null=True)

    history = HistoricalRecords()

    guardian_Type = models.ForeignKey(
        GuardianType, on_delete=models.CASCADE, blank=False
    )
    ident_type = models.ForeignKey(
        "IdentType", on_delete=models.CASCADE, blank=False
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Phone(models.Model):
    phone_name = models.CharField(max_length=255, blank=False)
    phone_number = models.IntegerField(blank=False, null=False)

    history = HistoricalRecords()

    phone_Feature = models.ForeignKey(
        PhoneFeature, on_delete=models.CASCADE, blank=False
    )
    guardian = models.ForeignKey(
        "Guardian", models.DO_NOTHING, db_column="Guardian_id", blank=False
    )  # Field name made lowercase.

    def __str__(self):
        return f"{self.phone_name}, {self.phone_number}"

class Payout(models.Model):
    amount = models.FloatField(blank=False)
    date = models.DateField(blank=False)
    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="Zone_id", blank=False
    )  # Field name made lowercase.

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}, {self.amount}, {self.date}"


class Shift(models.Model):
    name = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name}"


class Zone(models.Model):
    name = models.CharField(max_length=255, blank=False)

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Poll(models.Model):
    name =  models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

class Question(models.Model):
    description =  models.CharField(max_length=255, blank=False)
    parentQuestion = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    QUESTION_CHOICES = (
        ('Single Option', 'Single Option'),
        ('Single Choice', 'Single Choice'),
        ('Multiple Choice', 'Multiple Choice'),
    )
    questionType = models.CharField(max_length=255, blank=False, null=False, choices=QUESTION_CHOICES)
    poll = models.ForeignKey(
        "Poll", on_delete=models.CASCADE, blank=False, null=False
    )
    
    def __str__(self):
        return self.description

class Answer(models.Model):
    description = models.CharField(max_length=255, blank=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False, blank=False)
    ANSWER_CHOICES = (
        ('Boolean', 'Boolean'),
        ('Integer', 'Integer'),
        ('Float', 'Float'),
        ('String', 'String'),
    )
    answerType = models.CharField(max_length=255, blank=False, null=False, choices=ANSWER_CHOICES)

    def __str__(self):
        return self.description
    
    
    def save(self, *args, **kwargs):
        # Check if the associated question's questionType is 'Single Option'
        if self.question.questionType == 'Single Option':
            # Check if there is already an answer for this question
            existing_answer = Answer.objects.filter(question=self.question).first()
            if existing_answer and existing_answer != self:
                raise ValidationError("There can only be one answer for Single Option questions.")
        super().save(*args, **kwargs)




class ChildAnswer(models.Model):
    child = models.ForeignKey(
        "Child", on_delete=models.CASCADE, blank=False, null=False
    )
    answer = models.ForeignKey(
        "Answer", on_delete=models.CASCADE, blank=False, null=False
    )
    value =  models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"Child: {self.child}, Answer: {self.answer}"
    
    def save(self, *args, **kwargs):
        # Check if the associated question's questionType is 'Single Option'
        if self.answer.question.questionType in ('Single Option','Single Choice'):
            # Check if there is already an answer for this question
            existing_childAnswer = ChildAnswer.objects.filter(answer__question=self.answer.question, child = self.child).first()
            if existing_childAnswer and existing_childAnswer != self:
                raise ValidationError("There can only be one childAnswer for Single Option/Single Choice questions.")
        super().save(*args, **kwargs)

    # implementar mas adelante
    # def checkAnswerType(self):
    #     pass

    def returnValueAsAnswerType(self):
        
        selfAnswerType = self.answer.answerType
        selfValue = self.value
        valueReturn = bool(selfValue) if selfAnswerType == 'Boolean' else int(selfValue) if selfAnswerType == 'Integer' else float(selfValue) if selfAnswerType == 'Float' else str(selfValue)
            
        return valueReturn    

    

class TechnicalReport(models.Model):
    encabezado = models.CharField(max_length=255, blank=False, default="1983/2023 - 40 AÑOS DE DEMOCRACIA")
    ministro = models.CharField(max_length=255, blank=False, default="Sr. Ministro de Desarrollo Social Dr. Juan Carlos Massei")
    resolucion = models.CharField(max_length=255, blank=False, default="Resolución Ministerial N° 0007/2023")
    remitanse = models.CharField(max_length=255, blank=False, default="REMÍTANSE a la Subsecretaria de Administración y Recursos Humanos")
    history = HistoricalRecords()
    
    def save(self, *args, **kwargs):

        existing_obj = TechnicalReport.objects.first()

        if existing_obj:
            # Update the existing instance with the new values
            TechnicalReport.objects.filter(id=existing_obj.id).update(
                encabezado=self.encabezado,
                ministro=self.ministro,
                resolucion=self.resolucion,
                remitanse=self.remitanse
            )
        else:
            super(TechnicalReport, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Avoid deleting the object
        
        print('method not allowed')
        pass

    def __str__(self):
        return self.resolucion

