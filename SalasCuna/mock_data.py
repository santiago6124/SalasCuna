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
from SalasCuna_api.models import (
    Locality,
    Neighborhood,
    Child,
    ChildState,
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
    Role,
    Shift,
    Zone,
    Department,
)

fake = Faker()
User = get_user_model()


def create_users(num_users):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = "12345678"  # You can set a common password for all users
        User.objects.create_user(
            email=email, password=password, first_name=first_name, last_name=last_name
        )


def create_localities(num_localities):
    for _ in range(num_localities):
        locality = fake.city()
        Locality.objects.create(locality=locality)


def create_neighborhoods(num_neighborhoods):
    for _ in range(num_neighborhoods):
        neighborhood = fake.city_suffix()
        Neighborhood.objects.create(neighborhood=neighborhood)


def create_child_states():
    ChildState.objects.create(name="Active")
    ChildState.objects.create(name="Inactive")


def create_roles(num_roles):
    for _ in range(num_roles):
        name = fake.word()
        Role.objects.create(name=name)


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
        phone = fake.unique.random_number(digits=9)
        Company.objects.create(title=title, phone=phone)


def create_genders():
    Gender.objects.create(gender="Male")
    Gender.objects.create(gender="Female")
    Gender.objects.create(gender="10th generation Apache Helicopter")


def create_phone_features(num_features):
    for _ in range(num_features):
        feature = fake.random_int(min=100, max=999)
        PhoneFeature.objects.create(feature=feature)


def create_guardian_types():
    GuardianType.objects.create(type="Parent")
    GuardianType.objects.create(type="Guardian")


def create_cribroom(num_features):
    localities = Locality.objects.all()
    departments = Department.objects.all()
    neighborhoods = Neighborhood.objects.all()
    shifts = Shift.objects.all()
    zones = Zone.objects.all()
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
        )


def create_children(num_children):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    child_states = ChildState.objects.all()
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
        child_state = random.choice(child_states)

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
            child_state=child_state,
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
    roles = Role.objects.all()
    for _ in range(num_forms):
        generation_date = fake.date_between(start_date="-2y", end_date="today")
        cribroom_user = random.choice(cribroom_users)
        role = random.choice(roles)
        forms.append(
            Form(
                generation_date=generation_date, cribroom_user=cribroom_user, role=role
            )
        )
    Form.objects.bulk_create(forms)


def create_guardians(num_guardians):
    genders = Gender.objects.all()
    phone_features = PhoneFeature.objects.all()
    guardian_types = GuardianType.objects.all()
    for _ in range(num_guardians):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dni = fake.unique.random_number(digits=7)
        phone_number = fake.random_int(min=0, max=9999999)
        gender = random.choice(genders)
        phone_feature = random.choice(phone_features)
        guardian_type = random.choice(guardian_types)

        Guardian.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone_number=phone_number,
            gender=gender,
            phone_Feature=phone_feature,
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
num_users = 20
num_localities = 25
num_neighborhoods = 25
num_children = 10
num_companies = 10
num_cribroom = 15
num_cribroom_users = 10
num_departments = 25
num_desinfection = 5
num_forms = 10
num_phone_features = 25
num_guardians = 15
num_payouts = 10
num_roles = 25
num_shifts = 25
num_zones = 25

# Call the functions to create the mock data
create_localities(num_localities)
create_neighborhoods(num_neighborhoods)
create_child_states()
create_companies(num_companies)
create_genders()
create_phone_features(num_phone_features)
create_guardian_types()
create_guardians(num_guardians)
create_zones(num_zones)
create_departments(num_departments)
create_payouts(num_payouts)
create_roles(num_roles)
create_users(num_users)
create_shifts(num_shifts)
create_cribroom(num_cribroom)
create_cribroom_users(num_cribroom_users)
create_desinfections(num_desinfection)
create_forms(num_forms)
create_children(num_children)

print("Mock data has been successfully created.")
