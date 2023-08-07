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
)

fake = Faker()
User = get_user_model()

def create_users(num_users):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = "testpassword"  # You can set a common password for all users
        User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)

def create_localities(num_localities):
    for _ in range(num_localities):
        locality = fake.city()
        Locality.objects.create(locality=locality)

def create_neighborhoods(num_neighborhoods):
    for _ in range(num_neighborhoods):
        neighborhood = fake.city_suffix()
        Neighborhood.objects.create(neighborhood=neighborhood)

def create_child_states(num_states):
    states = ["Active", "Inactive"]
    for state in states[:num_states]:
        ChildState.objects.create(name=state)

def create_children(num_children):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    child_states = ChildState.objects.all()
    for _ in range(num_children):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dni = fake.unique.random_number(digits=11)
        birthdate = fake.date_of_birth()
        street = fake.street_name()
        house_number = fake.random_int(min=1, max=100)
        registration_date = fake.date_between(start_date="-2y", end_date="today")
        disenroll_date = fake.date_between(start_date=registration_date, end_date="today")
        locality = random.choice(localities)
        neighborhood = random.choice(neighborhoods)
        gender = Gender.objects.create(gender=random.choice(["Male", "Female"]))
        cribroom = Cribroom.objects.create(name=fake.city(), code=fake.random_int(min=1, max=100), max_capacity=fake.random_int(min=5, max=20))
        shift = Shift.objects.create(name=fake.word())
        user = User.objects.order_by('?').first()
        guardian = Guardian.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), dni=fake.unique.random_number(digits=11), phone_number=fake.unique.random_number(digits=9))
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

def create_companies(num_companies):
    for _ in range(num_companies):
        title = fake.company()
        phone = fake.unique.random_number(digits=9)
        Company.objects.create(title=title, phone=phone)

def create_cribroom_users(num_cribroom_users):
    cribrooms = Cribroom.objects.all()
    users = User.objects.all()
    for _ in range(num_cribroom_users):
        cribroom = random.choice(cribrooms)
        user = random.choice(users)
        CribroomUser.objects.create(cribroom=cribroom, user=user)

def create_desinfections(num_desinfections):
    desinfections = []
    cribrooms = Cribroom.objects.all()
    companies = Company.objects.all()
    for _ in range(num_desinfections):
        date = fake.date_time_this_year()
        description = fake.text()
        cribroom = random.choice(cribrooms)
        company = random.choice(companies)
        desinfections.append(Desinfection(date=date, description=description, cribroom=cribroom, company=company))
    Desinfection.objects.bulk_create(desinfections)

def create_forms(num_forms):
    forms = []
    cribroom_users = CribroomUser.objects.all()
    roles = Role.objects.all()
    for _ in range(num_forms):
        generation_date = fake.date_between(start_date="-2y", end_date="today")
        cribroom_user = random.choice(cribroom_users)
        role = random.choice(roles)
        forms.append(Form(generation_date=generation_date, cribroom_user=cribroom_user, role=role))
    Form.objects.bulk_create(forms)

def create_genders():
    genders = ["Male", "Female"]
    for gender in genders:
        Gender.objects.create(gender=gender)

def create_phone_features(num_features):
    for _ in range(num_features):
        feature = fake.random_int(min=1000, max=9999)
        PhoneFeature.objects.create(feature=feature)

def create_guardian_types(num_types):
    types = ["Parent", "Guardian"]
    for guardian_type in types[:num_types]:
        GuardianType.objects.create(type=guardian_type)

def create_guardians(num_guardians):
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    genders = Gender.objects.all()
    phone_features = PhoneFeature.objects.all()
    guardian_types = GuardianType.objects.all()
    for _ in range(num_guardians):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dni = fake.unique.random_number(digits=11)
        phone_number = fake.unique.random_number(digits=9)
        locality = random.choice(localities)
        neighborhood = random.choice(neighborhoods)
        gender = random.choice(genders)
        phone_feature = random.choice(phone_features)
        guardian_type = random.choice(guardian_types)

        Guardian.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone_number=phone_number,
            locality=locality,
            neighborhood=neighborhood,
            gender=gender,
            phone_Feature=phone_feature,
            guardian_Type=guardian_type,
        )

def create_payouts(num_payouts):
    payouts = []
    zones = Zone.objects.all()
    for _ in range(num_payouts):
        amount = fake.random_int(min=500, max=2000)
        date = fake.date_between(start_date="-1y", end_date="today")
        zone = random.choice(zones)
        payouts.append(Payout(amount=amount, date=date, zone=zone))
    Payout.objects.bulk_create(payouts)

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

# Set the number of instances you want to create for each model
num_users = 10
num_localities = 5
num_neighborhoods = 5
num_child_states = 2
num_children = 20
num_companies = 5
num_cribroom_users = 10
num_desinfections = 15
num_forms = 10
num_genders = 2
num_phone_features = 5
num_guardian_types = 2
num_guardians = 15
num_payouts = 10
num_roles = 5
num_shifts = 3
num_zones = 5

# Call the functions to create the mock data
create_users(num_users)
create_localities(num_localities)
create_neighborhoods(num_neighborhoods)
create_child_states(num_child_states)
create_children(num_children)
create_companies(num_companies)
create_cribroom_users(num_cribroom_users)
create_desinfections(num_desinfections)
create_forms(num_forms)
create_genders()
create_phone_features(num_phone_features)
create_guardian_types(num_guardian_types)
create_guardians(num_guardians)
create_payouts(num_payouts)
create_roles(num_roles)
create_shifts(num_shifts)
create_zones(num_zones)

print("Mock data has been successfully created.")
