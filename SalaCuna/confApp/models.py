# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
        

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_lenght=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class Addresses(models.Model):
    street = models.CharField(max_length=150, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    district = models.ForeignKey('Districts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Answers(models.Model):
    answer = models.CharField(max_length=200, blank=True, null=True)
    question = models.ForeignKey('Questions', models.DO_NOTHING, blank=True, null=True)
    form = models.ForeignKey('Forms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Children(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=40, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    disenroll_date = models.DateField(blank=True, null=True)
    gender = models.ForeignKey('Genders', models.DO_NOTHING, blank=True, null=True)
    cribroom = models.ForeignKey('Cribrooms', models.DO_NOTHING, blank=True, null=True)
    shift = models.ForeignKey('Shifts', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    guardian = models.ForeignKey('Guardians', models.DO_NOTHING, blank=True, null=True)
    children_state = models.ForeignKey('ChildrenState', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'children'


class ChildrenState(models.Model):
    active = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'children_state'


class Cribrooms(models.Model):
    max_capacity = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    zone = models.ForeignKey('Zones', models.DO_NOTHING, blank=True, null=True)
    shift = models.ForeignKey('Shifts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cribrooms'


class Departments(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Desinfections(models.Model):
    desinfection_date = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    company_phone = models.CharField(max_length=100, blank=True, null=True)
    cribroom = models.ForeignKey(Cribrooms, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'desinfections'


class Districts(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    locality = models.ForeignKey('Localities', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Forms(models.Model):
    generation_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cribroom = models.ForeignKey(Cribrooms, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forms'


class Genders(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genders'


class GuardianPhones(models.Model):
    phone_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guardian_phones'


class Guardians(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=40, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    phone = models.ForeignKey(GuardianPhones, models.DO_NOTHING, blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guardians'


class Localities(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localities'


class Options(models.Model):
    question = models.ForeignKey('Questions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class Padrones(models.Model):
    generation_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'padrones'


class Paynote(models.Model):
    generation_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    payout = models.ForeignKey('Payouts', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paynote'


class Payouts(models.Model):
    date = models.DateField(blank=True, null=True)
    upcountry = models.IntegerField(blank=True, null=True)
    capital = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payouts'


class QuestionTypes(models.Model):
    question_type = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_types'


class Questions(models.Model):
    question = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    question_types = models.ForeignKey(QuestionTypes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class Roles(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Shifts(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shifts'


class UserEmails(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_emails'


class Users(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.ForeignKey(UserEmails, models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Zones(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones'
