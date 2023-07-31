import random
from datetime import date
from django.utils import timezone
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SalasCuna.settings")

# Initialize Django
django.setup()

# Now you can import the models and perform data population
from SalasCuna_api.models import (
    Locality,
    Neighborhood,
    Child,
    ChildState,
    Cribroom,
    Gender,
    PhoneFeature,
    GuardianType,
    Guardian,
    Shift,
    Zone,
)
def create_mock_localities():
    localities = ['Locality A', 'Locality B', 'Locality C']
    for locality in localities:
        Locality.objects.create(locality=locality)

def create_mock_neighborhoods():
    neighborhoods = ['Neighborhood 1', 'Neighborhood 2', 'Neighborhood 3']
    for neighborhood in neighborhoods:
        Neighborhood.objects.create(neighborhood=neighborhood)

def create_mock_child_states():
    child_states = ['State 1', 'State 2', 'State 3']
    for state in child_states:
        ChildState.objects.create(name=state)

def create_mock_genders():
    genders = ['Male', 'Female']
    for gender in genders:
        Gender.objects.create(gender=gender)

def create_mock_phone_features():
    features = [1, 2, 3, 4]
    for feature in features:
        PhoneFeature.objects.create(feature=feature)

def create_mock_guardian_types():
    types = ['Type A', 'Type B', 'Type C']
    for guardian_type in types:
        GuardianType.objects.create(type=guardian_type)

def create_mock_shifts():
    shifts = ['Morning', 'Afternoon', 'Evening']
    for shift_name in shifts:
        shift, created = Shift.objects.get_or_create(name=shift_name)
        if created:
            print(f"Created Shift: {shift}")

def create_mock_zones():
    zones = ['Zone 1', 'Zone 2', 'Zone 3']
    for zone in zones:
        Zone.objects.create(name=zone)

def create_mock_cribrooms():
    for i in range(1, 4):
        Cribroom.objects.create(
            name=f"Cribroom {i}",
            code=i,
            max_capacity=random.randint(5, 15),
            adress=None,  # Replace with actual address data if available
            zone=Zone.objects.get(name=f"Zone {i}"),
            shift=Shift.objects.get(name=f"Shift {i}"),
        )

def create_mock_children(num_children=10):
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Julia']
    last_names = ['Smith', 'Johnson', 'Brown', 'Lee', 'Davis', 'Wilson', 'Garcia', 'Martinez', 'Miller', 'Taylor']
    localities = Locality.objects.all()
    neighborhoods = Neighborhood.objects.all()
    genders = Gender.objects.all()
    cribrooms = Cribroom.objects.all()
    shifts = Shift.objects.all()
    child_states = ChildState.objects.all()

    for _ in range(num_children):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        dni = str(random.randint(10000000, 99999999))
        birthdate = date.today() - timezone.timedelta(days=random.randint(1000, 5000))
        street = f"Street {random.randint(1, 100)}"
        house_number = random.randint(1, 100)
        registration_date = date.today() - timezone.timedelta(days=random.randint(1, 365))
        disenroll_date = date.today() - timezone.timedelta(days=random.randint(1, 365))
        locality = random.choice(localities)
        neighborhood = random.choice(neighborhoods)
        gender = random.choice(genders)
        cribroom = random.choice(cribrooms)
        shift = random.choice(shifts)
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
            child_state=child_state,
        )

def create_mock_guardians(num_guardians=10):
    first_names = ['John', 'Mary', 'Michael', 'Emma', 'James', 'Sophia', 'William', 'Olivia', 'Alexander', 'Ava']
    last_names = ['Jones', 'Brown', 'Davis', 'Garcia', 'Miller', 'Taylor', 'Anderson', 'Thomas', 'Wilson', 'Harris']
    genders = Gender.objects.all()
    phone_features = PhoneFeature.objects.all()
    guardian_types = GuardianType.objects.all()

    for _ in range(num_guardians):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        dni = str(random.randint(10000000, 99999999))
        phone_number = random.randint(1000000000, 9999999999)
        phone_feature = random.choice(phone_features)
        guardian_type = random.choice(guardian_types)
        gender = random.choice(genders)

        Guardian.objects.create(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone_number=phone_number,
            phone_Feature=phone_feature,
            guardian_Type=guardian_type,
            gender=gender,
        )

def create_mock_data():
    create_mock_localities()
    create_mock_neighborhoods()
    create_mock_child_states()
    create_mock_genders()
    create_mock_phone_features()
    create_mock_guardian_types()
    create_mock_shifts()
    create_mock_zones()
    create_mock_cribrooms()
    create_mock_children()
    create_mock_guardians()

# Run this function to populate the database with mock data
create_mock_data()
