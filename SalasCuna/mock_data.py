import random
from datetime import date
from django.utils import timezone
import os
import django

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
    Co_managment
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
        co_managment = fake.city()
        Co_managment.objects.create(co_managment=co_managment)


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


def create_guardian_types():
    GuardianType.objects.create(type="Parent")
    GuardianType.objects.create(type="Guardian")


def create_cribroom(num_features):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    co_managments = Co_managment.objects.all()
    sectionals = Sectional.objects.all()
    users = User.objects.all()
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
            co_managment = random.choice(co_managments),
            sectional = random.choice(sectionals),
            user=random.choice(users),
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
            user=user,
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


def create_payouts(num_payouts):
    zones = Zone.objects.all()
    for _ in range(num_payouts):
        amount = fake.random_int(min=15000, max=85000)
        date = fake.date_between(start_date="-1y", end_date="today")
        zone = random.choice(zones)
        Payout.objects.create(amount=amount, date=date, zone=zone)


# Set the number of instances you want to create for each model
nueve = 9
veinte = 20
diez = 10
quince = 15
cinco = 5

# Call the functions to create the mock data
create_identType()
create_zones(veinte)
create_departments(veinte)
create_localities(veinte)
create_neighborhoods(veinte)
create_companies(diez)
create_genders()
create_phone_features(veinte)
create_guardian_types()
create_guardians(quince)
create_coManagment(veinte)
create_seccional(veinte)
for i in range(15):
    create_payouts(diez)
create_groups()
create_users(nueve)
create_superuser()
create_shifts(veinte)
create_cribroom(quince)
create_cribroom_users(diez)
for i in range(20):
    create_desinfections(cinco)
create_forms(diez)
create_identType()
for i in range(50):
    create_children(diez)

print("Mock data has been successfully created.")
