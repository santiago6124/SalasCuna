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


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    """         "first_name": e.target.first_name.value,
                "last_name": e.target.last_name.value,
                "dni": e.target.dni.value,
                "role": e.target.role.value,
                "phone_number": e.target.phone_number.value,
                "address": e.target.address.value,
                "department": e.target.department.value,
                "city": e. target.city.value,
                "email": e.target.email.value,
                "password": e.target.password.value,
                "re_password": e.target.re_password.value
    """

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.email}, ({self.last_name}, {self.first_name})"


class Adress(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.name


class Locality(models.Model):
    locality = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.locality

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.neighborhood

class Child(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    street = models.CharField(max_length=255, blank=True, null=True)
    house_number = models.IntegerField(blank=True, null=True)

    registration_date = models.DateField(blank=True, null=True)
    disenroll_date = models.DateField(blank=True, null=True)

    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, blank=True, null=True)

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
        "User", models.DO_NOTHING, db_column="User_id", blank=True, null=True
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




    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class ChildState(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)




    def __str__(self):
        return self.title


class Cribroom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)
    max_capacity = models.IntegerField(blank=True, null=True)
    adress = models.ForeignKey(
        Adress, models.DO_NOTHING, db_column="Adress_id", blank=True, null=True
    )  # Field name made lowercase.
    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="Zone_id", blank=True, null=True
    )  # Field name made lowercase.
    shift = models.ForeignKey(
        "Shift", models.DO_NOTHING, db_column="Shift_id", blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return f"Zone:{self.name}, Max:{self.code}"


class CribroomUser(models.Model):
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    user = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="User_id", blank=True, null=True
    )  # Field name made lowercase.




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




    def __str__(self):
        return f"{self.id}, {self.generation_date}"


class Gender(models.Model):
    gender = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.gender


class PhoneFeature(models.Model):
    feature = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.feature

class GuardianType(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.type


class Guardian(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    
    phone_number =  models.IntegerField(blank=True, null=True)    
    
    phone_Feature = models.ForeignKey(PhoneFeature, on_delete=models.CASCADE, blank=True, null=True)
    guardian_Type = models.ForeignKey(GuardianType, on_delete=models.CASCADE, blank=True, null=True)

    gender = models.ForeignKey(
        Gender, models.DO_NOTHING, db_column="Gender_id", blank=True, null=True
    )  # Field name made lowercase.


    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Payout(models.Model):
    amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="Zone_id", blank=True, null=True
    )  # Field name made lowercase.




    def __str__(self):
        return f"{self.id}, {self.amount}"


class Role(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.ForeignKey(
        "UserEmail", models.DO_NOTHING, db_column="User_email_id", blank=True, null=True
    )  # Field name made lowercase.
    role = models.ForeignKey(
        Role, models.DO_NOTHING, db_column="Role_id", blank=True, null=True
    )  # Field name made lowercase.




    def __str__(self):
        return f"{self.username}, {self.user_email}"


class UserEmail(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.email


class Zone(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)




    def __str__(self):
        return self.name
