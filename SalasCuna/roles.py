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
    UserAccount,
)

fake = Faker()
User = get_user_model()

def create_roles(num_roles):
    for i in range(num_roles):
        name = f"pepe{i}"
        Role.objects.create(name=name)
        print(name)

def create_users(num_users):
    for i in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = "testpassword"  # You can set a common password for all users
        role = Role.objects.get(id= i + 1)
        UserAccount.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, role=role)
        print("created user")
        print("assigned role")
         

num_roles = 3
num_users = 3

#create_roles(num_roles)
create_users(num_users)
