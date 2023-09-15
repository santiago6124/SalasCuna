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
    PhoneGuardian,
    PhoneUser,
    PhoneCompany,
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
            address=address,
            department=department,
            city=city,
        )


def create_localities(num_localities):
    for _ in range(num_localities):
        locality = fake.city()
        Locality.objects.create(locality=locality)


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


def create_departments(num_departments):
    for _ in range(num_departments):
        name = fake.city()
        Department.objects.create(department=name)


def create_companies(num_companies):
    for _ in range(num_companies):
        title = fake.company()
        Company.objects.create(title=title)


def create_genders():
    Gender.objects.create(gender="Male")
    Gender.objects.create(gender="Female")
    Gender.objects.create(gender="10th generation Apache Helicopter")


def create_phone_features(num_features):
    for _ in range(num_features):
        feature = fake.random_int(min=310, max=380)
        PhoneFeature.objects.create(feature=feature)


def create_guardianPhones(num_phones):
    guardians = Guardian.objects.all()
    phone_features = PhoneFeature.objects.all()
    for _ in range(num_phones):
        PhoneGuardian.objects.create(
            number=fake.unique.random_number(digits=7),
            guardian=random.choice(guardians),
            phone_feature=random.choice(phone_features),
        )


def create_userPhones(num_phones):
    users = User.objects.all()
    phone_features = PhoneFeature.objects.all()
    for _ in range(num_phones):
        PhoneUser.objects.create(
            number=fake.unique.random_number(digits=7),
            user=random.choice(users),
            phone_feature=random.choice(phone_features),
        )


def create_companyPhones(num_phones):
    companies = Company.objects.all()
    phone_features = PhoneFeature.objects.all()
    for _ in range(num_phones):
        PhoneCompany.objects.create(
            number=fake.unique.random_number(digits=7),
            company=random.choice(companies),
            phone_feature=random.choice(phone_features),
        )


def create_guardian_types():
    GuardianType.objects.create(type="Parent")
    GuardianType.objects.create(type="Guardian")


def create_cribroom(num_features):
    localities = Locality.objects.all()
    departments = Department.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    zones = Zone.objects.all()
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
            locality=random.choice(localities),
            department=random.choice(departments),
            neighborhood=random.choice(neighborhoods),
            shift=random.choice(shifts),
            zone=random.choice(zones),
            user=random.choice(users),
        )


def create_children(num_children):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    cribrooms = Cribroom.objects.all()
    guardians = Guardian.objects.all()
    genders = Gender.objects.all()
    for _ in range(num_children):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dni = fake.unique.random_number(digits=8)
        birthdate = fake.date_of_birth()
        street = fake.street_name()
        house_number = fake.random_int(min=1, max=6000)
        registration_date = fake.date_between(start_date="-2y", end_date="today")
        disenroll_date = fake.date_between(
            start_date=registration_date, end_date="today"
        )
        locality = random.choice(localities)
        neighborhood = random.choice(neighborhoods)
        gender = random.choice(genders)
        cribroom = random.choice(cribrooms)
        shift = random.choice(shifts)
        user = User.objects.order_by("?").first()
        guardian = random.choice(guardians)

        Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            birthdate=birthdate,
            street=street,
            house_number=house_number,
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
    genders = Gender.objects.all()
    guardian_types = GuardianType.objects.all()
    for _ in range(num_guardians):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dni = fake.unique.random_number(digits=7)
        gender = random.choice(genders)
        guardian_type = random.choice(guardian_types)

        Guardian.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            gender=gender,
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
num_users = 9
num_localities = 20
num_neighborhoods = 20
num_children = 10
num_companies = 10
num_cribroom = 15
num_cribroom_users = 10
num_departments = 20
num_desinfection = 5
num_forms = 10
num_phone_features = 20
num_guardianPhone = 10
num_userPhone = 10
num_companyPhone = 7
num_guardians = 15
num_payouts = 10
num_shifts = 20
num_zones = 20

# Call the functions to create the mock data
create_localities(num_localities)
create_neighborhoods(num_neighborhoods)
create_companies(num_companies)
create_genders()
create_phone_features(num_phone_features)
create_guardian_types()
create_guardians(num_guardians)
create_zones(num_zones)
create_departments(num_departments)
for i in range(15):
    create_payouts(num_payouts)
create_groups()
create_users(num_users)
for i in range(20):
    create_guardianPhones(num_guardianPhone)
    create_userPhones(num_userPhone)
    create_companyPhones(num_companyPhone)
create_shifts(num_shifts)
create_cribroom(num_cribroom)
create_cribroom_users(num_cribroom_users)
for i in range(20):
    create_desinfections(num_desinfection)
create_forms(num_forms)
for i in range(50):
    create_children(num_children)

print("Mock data has been successfully created.")
