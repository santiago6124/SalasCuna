# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from simple_history.models import HistoricalRecords
from num2words import num2words

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
    role = models.ForeignKey(
        "Role", on_delete=models.CASCADE, db_column="Role_id", blank=True, null=True
    )
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    history = HistoricalRecords()

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.email}, ({self.last_name}, {self.first_name})"


class Locality(models.Model):
    locality = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.locality}"


class Department(models.Model):
    department = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.department}"

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.neighborhood}"


class Child(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.IntegerField(blank=True, null=True)

    registration_date = models.DateField(blank=True, null=True)
    disenroll_date = models.DateField(blank=True, null=True)

    locality = models.ForeignKey(
        Locality, on_delete=models.CASCADE, blank=True, null=True
    )
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, null=True
    )

    gender = models.ForeignKey(
        "Gender", models.DO_NOTHING, db_column="Gender_id", blank=True, null=True
    )  # Field name made lowercase.
    cribroom = models.ForeignKey(
        "Cribroom", models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    shift = models.ForeignKey(
        "Shift", models.DO_NOTHING, db_column="Shift_id", blank=True, null=True
    )  # Field name made lowercase.
    user = models.ForeignKey(
        "UserAccount", models.DO_NOTHING, db_column="User_id", blank=True, null=True
    )  # Field name made lowercase.
    guardian = models.ForeignKey(
        "Guardian", models.DO_NOTHING, db_column="Guardian_id", blank=True, null=True
    )  # Field name made lowercase.
    child_state = models.ForeignKey(
        "ChildState",
        models.DO_NOTHING,
        db_column="Child_state_id",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class ChildState(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title


class Cribroom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    entity = models.CharField(max_length=255, blank=True, null=True)
    CUIT = models.BigIntegerField(blank=True, null=True)  # nuevos campos
    code = models.IntegerField(blank=True, null=True)

    max_capacity = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.IntegerField(blank=True, null=True)

    locality = models.ForeignKey(
        Locality, on_delete=models.CASCADE, blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, blank=True, null=True
    )
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, null=True
    )

    shift = models.ForeignKey(
        "Shift", models.DO_NOTHING, db_column="Shift_id", blank=True, null=True
    )  # Field name made lowercase.

    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="zone_id", blank=True, null=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return f"Zone: {self.name}, Max: {self.max_capacity}, COD: {self.code}, CUIT: {self.CUIT}"
    
    def totalImport(self, init_date, end_date):
        '''
        calcular en base a maximo de chico x valor por mes durante los siguientes 12 meses
        
        for n in 12_months:
            month_import_n = max_capacity * amount
        '''
        try:
            payouts = Payout.objects.filter(zone = self.zone.id, date__range=[init_date, end_date])
            print(f'payouts: {payouts}')
            min_date = min(payouts, key=lambda payout: payout.date).date
            max_date = max(payouts, key=lambda payout: payout.date).date
           
            pays = {}
            
            pays['totalSumEndMonth'] = max_date.month
            pays['totalSumEndYear'] = max_date.year
            pays['totalSumInitMonth'] = min_date.month
            pays['totalSumInitYear'] = min_date.year

            for payout in payouts:
                pays[str(payout.date)] = payout.amount * self.max_capacity

                try:
                    pays[str(payout.date.year)] += payout.amount * self.max_capacity
                except:
                    pays[str(payout.date.year)] = payout.amount * self.max_capacity
                    
                try:
                    pays['totalSumFloat'] += payout.amount * self.max_capacity
                    pays['totalSumStr'] = num2words(pays['totalSumFloat'], lang='es')
                except:
                    pays['totalSumFloat'] = payout.amount * self.max_capacity
                    pays['totalSumStr'] = num2words(pays['totalSumFloat'], lang='es')

                try:
                    pays['firstSubTotalSumFloat'] += payout.amount * self.max_capacity if payout.date.year <= pays['totalSumInitYear'] else 0
                    
                except:
                    pays['firstSubTotalSumFloat'] = payout.amount * self.max_capacity if payout.date.year <= pays['totalSumInitYear'] else 0
                    
                try:
                    pays['SecSubTotalSumFloat'] += payout.amount * self.max_capacity if payout.date.year >= pays['totalSumEndYear'] else 0
                except:
                    pays['SecSubTotalSumFloat'] = payout.amount * self.max_capacity if payout.date.year >= pays['totalSumEndYear'] else 0
                    
                try:
                    pays['firstSubTotalSumEndMonth'] = payout.date.month if payout.date.year <= pays['totalSumInitYear'] and payout.date.month >= pays['firstSubTotalSumEndMonth'] else pays['firstSubTotalSumEndMonth'] 
                except:
                    pays['firstSubTotalSumEndMonth'] = payout.date.month if payout.date.year <= pays['totalSumInitYear'] else 100

                try:
                    pays['SecSubTotalSumInitMonth'] = payout.date.month if payout.date.year >= pays['totalSumEndYear'] and payout.date.month <= pays['SecSubTotalSumInitMonth'] else pays['SecSubTotalSumInitMonth'] 
                except:
                    pays['SecSubTotalSumInitMonth'] = payout.date.month if payout.date.year >= pays['totalSumEndYear'] else 100


            month_names_spanish = {
                1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
                7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
            }

            pays['totalSumEndMonth'] = month_names_spanish[pays['totalSumEndMonth']]
            pays['totalSumInitMonth'] = month_names_spanish[pays['totalSumInitMonth']]
            pays['firstSubTotalSumEndMonth'] = month_names_spanish[pays['firstSubTotalSumEndMonth']]
            pays['SecSubTotalSumInitMonth'] = month_names_spanish[pays['SecSubTotalSumInitMonth']]

        except Exception as e:
            return f'An error ocurred: {e}'

        return pays
    
    def maxCapacityStr(self):
        return num2words(self.max_capacity, lang='es')


class CribroomUser(models.Model):
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    user = models.ForeignKey(
        "UserAccount", models.DO_NOTHING, db_column="User_id", blank=True, null=True
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user}, {self.cribroom}"


class Desinfection(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column="Company_id", blank=True, null=True
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.cribroom}, {self.date}"


class Form(models.Model):
    generation_date = models.DateField(blank=True, null=True)
    cribroom_user = models.ForeignKey(
        CribroomUser,
        models.DO_NOTHING,
        db_column="Cribroom_User_id",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    role = models.ForeignKey(
        "Role", models.DO_NOTHING, db_column="Role_id", blank=True, null=True
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}, {self.generation_date}"


class Gender(models.Model):
    gender = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.gender}"


class PhoneFeature(models.Model):
    feature = models.IntegerField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.feature}"


class GuardianType(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.type}"


class Guardian(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)

    phone_number = models.IntegerField(blank=True, null=True)

    phone_Feature = models.ForeignKey(
        PhoneFeature, on_delete=models.CASCADE, blank=True, null=True
    )
    guardian_Type = models.ForeignKey(
        GuardianType, on_delete=models.CASCADE, blank=True, null=True
    )

    gender = models.ForeignKey(
        Gender, models.DO_NOTHING, db_column="Gender_id", blank=True, null=True
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Payout(models.Model):
    amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="Zone_id", blank=True, null=True
    )  # Field name made lowercase.
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.id}, {self.amount}, {self.date}"


class Role(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name}"


class Zone(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
