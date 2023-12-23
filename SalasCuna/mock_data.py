import random
from datetime import date, datetime
from django.utils import timezone
import os
import django

from django.core.exceptions import ValidationError
from django.db import IntegrityError

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SalasCuna.settings")

# Initialize Django
django.setup()

import random
from faker import Faker
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from SalasCuna_api.models import (
    Locality,
    Neighborhood,
    Child,
    Company,
    Cribroom,
    CribroomUser,
    Desinfection,
    Form,
    Gender,
    PhoneFeature,
    GuardianType,
    Guardian,
    Payout,
    Shift,
    Zone,
    Department,
    IdentType,
    Sectional,
    Co_management,
    ChildAnswer,
    Answer,
    Question,
    Poll,
    Phone,
    TechnicalReport,
    PayNote,
)

fake = Faker()
User = get_user_model()


def create_users(num_users):
    departments = Department.objects.all()
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        dni = fake.unique.random_number(digits=7)
        phone_number = fake.random_int(min=0, max=9999999)
        address = fake.street_name()
        department = random.choice(departments)
        city = fake.city()
        password = "12345678"  # You can set a common password for all users
        User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone_number=phone_number,
            address=address,
            department=department,
            city=city,
        )

def create_superuser():
    departments = Department.objects.all()
    first_name = "Admin"
    last_name = "Admin"
    email = "a@gmail.com"
    dni = fake.unique.random_number(digits=7)
    phone_number = fake.random_int(min=0, max=9999999)
    address = fake.street_name()
    department = random.choice(departments)
    city = fake.city()
    password = "pepe1234"  # You can set a common password for all users
    User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        dni=dni,
        phone_number=phone_number,
        address=address,
        department=department,
        city=city,
    )


def create_localities(num_localities):
    departments = Department.objects.all()
    for _ in range(num_localities):
        locality = fake.city()
        department = random.choice(departments)
        Locality.objects.create(locality=locality, department=department)


def create_neighborhoods(num_neighborhoods):
    for _ in range(num_neighborhoods):
        neighborhood = fake.city_suffix()
        Neighborhood.objects.create(neighborhood=neighborhood)


def create_groups():
    grupos = [
        "Director",
        "Trabajador Social",
        "Arquitecto",
        "Dev",
        "Psicopedagoga",
        "Administrador",
        "Secretario",
        "CoordinadorTS",
    ]
    for grupo in grupos:
        Group.objects.create(name=grupo)


def create_shifts(num_shifts):
    for _ in range(num_shifts):
        name = fake.word()
        Shift.objects.create(name=name)


def create_zones(num_zones):
    for _ in range(num_zones):
        name = fake.city()
        Zone.objects.create(name=name)


def create_seccional(num_seccional):
    for _ in range(num_seccional):
        sectional = fake.city()
        Sectional.objects.create(sectional=sectional)
        

def create_coManagment(num_coManagment):
    for _ in range(num_coManagment):
        co_management = fake.city()
        Co_management.objects.create(co_management=co_management)


def create_departments(num_departments):
    zones = Zone.objects.all()
    for _ in range(num_departments):
        name = fake.city()
        zone = random.choice(zones)
        Department.objects.create(department=name, zone=zone)


def create_companies(num_companies):
    for _ in range(num_companies):
        title = fake.company()
        phone = fake.unique.random_number(digits=9)
        Company.objects.create(title=title, phone=phone)


def create_genders():
    Gender.objects.create(gender="Male")
    Gender.objects.create(gender="Female")
    # Gender.objects.create(gender="10th generation Apache Helicopter")


def create_phone_features(num_features):
    for _ in range(num_features):
        feature = fake.random_int(min=100, max=999)
        PhoneFeature.objects.create(feature=feature)


def create_phone(num_phones):
    phoneFeatures = PhoneFeature.objects.all()
    guardians = Guardian.objects.all()
    for _ in range(num_phones):
        phone_name = fake.word()
        phone_number = fake.random_int(min= 2000000, max=9999999)
        Phone.objects.create(
            phone_name=phone_name,
            phone_number=phone_number,
            phone_Feature=random.choice(phoneFeatures),
            guardian = random.choice(guardians)
        )


def create_guardian_types():
    GuardianType.objects.create(type="Parent")
    GuardianType.objects.create(type="Guardian")


def create_cribroom(num_features):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    co_managements = Co_management.objects.all()
    sectionals = Sectional.objects.all()
    for _ in range(num_features):
        Cribroom.objects.create(
            name=fake.city(),
            code=fake.random_int(min=1, max=999),
            entity=fake.word(),
            CUIT=fake.random_int(min=10000, max=50000),
            max_capacity=fake.random_int(min=50, max=600),
            street=fake.street_name(),
            house_number=fake.random_int(min=1, max=6000),
            geolocation = (fake.random_int(min=-179, max=180), fake.random_int(min=-179, max=180)),
            locality=random.choice(localities),
            neighborhood=random.choice(neighborhoods),
            shift=random.choice(shifts),
            co_management = random.choice(co_managements),
            sectional = random.choice(sectionals),
        )

def create_identType():
    IdentType.objects.create(type="Pasaporte")
    IdentType.objects.create(type="DNI")
    IdentType.objects.create(type="Indocumentado")


def create_children(num_children):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    cribrooms = Cribroom.objects.all()
    guardians = Guardian.objects.all()
    genders = Gender.objects.all()
    identTypes = IdentType.objects.all()
    for _ in range(num_children):
        first_name = fake.first_name()
        last_name = fake.last_name()
        identification = fake.unique.random_number(digits=8)
        birthdate = fake.date_of_birth()
        street = fake.street_name()
        house_number = fake.random_int(min=1, max=6000)
        registration_date = fake.date_between(start_date="-2y", end_date="today")
        disenroll_date = fake.date_between(
            start_date=registration_date, end_date="today"
        )
        geolocation = (fake.random_int(min=-179, max=180), fake.random_int(min=-179, max=180))
        locality = random.choice(localities)
        neighborhood = random.choice(neighborhoods)
        gender = random.choice(genders)
        cribroom = random.choice(cribrooms)
        shift = random.choice(shifts)
        identType = random.choice(identTypes)
        user = User.objects.order_by("?").first()
        guardian = random.choice(guardians)

        Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            identification=identification,
            ident_type=identType,
            birthdate=birthdate,
            street=street,
            house_number=house_number,
            geolocation=geolocation,
            registration_date=registration_date,
            disenroll_date=disenroll_date,
            locality=locality,
            neighborhood=neighborhood,
            gender=gender,
            cribroom=cribroom,
            shift=shift,
            guardian=guardian,
        )


def create_cribroom_users(num_cribroom_users):
    cribrooms = Cribroom.objects.all()
    users = User.objects.all()
    for _ in range(num_cribroom_users):
        cribroom = random.choice(cribrooms)
        user = random.choice(users)
        CribroomUser.objects.create(cribroom=cribroom, user=user)


def create_desinfections(num_desinfections):
    cribrooms = Cribroom.objects.all()
    companies = Company.objects.all()
    for _ in range(num_desinfections):
        date = fake.date_between(start_date="-2y", end_date="today")
        description = fake.word()
        cribroom = random.choice(cribrooms)
        company = random.choice(companies)
        Desinfection.objects.create(
            date=date, description=description, cribroom=cribroom, company=company
        )


def create_forms(num_forms):
    forms = []
    cribroom_users = CribroomUser.objects.all()
    for _ in range(num_forms):
        generation_date = fake.date_between(start_date="-2y", end_date="today")
        cribroom_user = random.choice(cribroom_users)
        forms.append(Form(generation_date=generation_date, cribroom_user=cribroom_user))
    Form.objects.bulk_create(forms)


def create_guardians(num_guardians):
    identTypes = IdentType.objects.all()
    guardian_types = GuardianType.objects.all()
    for _ in range(num_guardians):
        first_name = fake.first_name()
        last_name = fake.last_name()
        identification = fake.unique.random_number(digits=7)
        ident_type = random.choice(identTypes)
        guardian_type = random.choice(guardian_types)

        Guardian.objects.create(
            first_name=first_name,
            last_name=last_name,
            identification=identification,
            ident_type=ident_type,
            guardian_Type=guardian_type,
        )


def validate_date_format(value):
    try:
        datetime.strptime(value, '%Y-%m')
    except ValueError:
        raise ValidationError('El formato de fecha debe ser YYYY-MM')

def create_payouts(num_payouts):
    zones = Zone.objects.all()
    for _ in range(num_payouts):
        amount = fake.random_int(min=15000, max=85000)
        date = fake.date_between(start_date="-1y", end_date="today").strftime('%Y-%m')
        zone = random.choice(zones)

        try:
            # Try to create the Payout object
            Payout.objects.create(amount=amount, date=date, zone=zone)
        except IntegrityError as e:
            # Catch IntegrityError, which includes ValidationError for unique constraint
            if 'unique constraint' in str(e):
                print(f"Skipping creation of duplicate payout for zone {zone} and date {date}")
            else:
                # Re-raise the exception if it's not related to uniqueness
                raise e
        except ValidationError as e:
            # Catch and print the validation error
            print(f"Validation error: {e}")


# Call the functions to create the mock data
create_identType()
create_zones(20)
create_departments(20)
create_localities(20)
create_neighborhoods(20)
create_companies(10)
create_genders()
create_phone_features(20)
create_guardian_types()
create_guardians(15)
create_phone(10)
create_coManagment(20)
create_seccional(20)
for i in range(15):
    create_payouts(10)
create_groups()
create_users(9)
create_superuser()
create_shifts(20)
create_cribroom(15)
create_cribroom_users(10)
for i in range(20):
    create_desinfections(5)
create_forms(10)
create_identType()
for i in range(10):
    create_children(10)

TechnicalReport.objects.create()
PayNote.objects.create()

print("Mock data has been successfully created.")
