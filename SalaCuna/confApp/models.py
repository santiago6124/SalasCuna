# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adress(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "adress"


class Child(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    disenroll_date = models.DateField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = "child"


class ChildState(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "child_state"


class Company(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "company"


class Cribroom(models.Model):
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

    class Meta:
        managed = False
        db_table = "cribroom"


class CribroomUser(models.Model):
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    user = models.ForeignKey(
        "User", models.DO_NOTHING, db_column="User_id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "cribroom_user"


class Desinfection(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    cribroom = models.ForeignKey(
        Cribroom, models.DO_NOTHING, db_column="Cribroom_id", blank=True, null=True
    )  # Field name made lowercase.
    company = models.ForeignKey(
        Company, models.DO_NOTHING, db_column="Company_id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "desinfection"


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

    class Meta:
        managed = False
        db_table = "form"


class Gender(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "gender"


class Guardian(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    dni = models.CharField(max_length=255, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    guardian_phone = models.ForeignKey(
        "GuardianPhone",
        models.DO_NOTHING,
        db_column="Guardian_phone_id",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    gender = models.ForeignKey(
        Gender, models.DO_NOTHING, db_column="Gender_id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "guardian"


class GuardianPhone(models.Model):
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "guardian_phone"


class Payout(models.Model):
    amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    zone = models.ForeignKey(
        "Zone", models.DO_NOTHING, db_column="Zone_id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "payout"


class Role(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "role"


class Shift(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "shift"


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.ForeignKey(
        "UserEmail", models.DO_NOTHING, db_column="User_email_id", blank=True, null=True
    )  # Field name made lowercase.
    role = models.ForeignKey(
        Role, models.DO_NOTHING, db_column="Role_id", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "user"


class UserEmail(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "user_email"


class Zone(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "zone"
