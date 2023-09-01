import unittest
from datetime import date

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SalasCuna.settings")

django.setup()

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


class TestChildModel(unittest.TestCase):

    def setUp(self):
        self.locality = Locality.objects.create(locality="Test Locality")
        self.neighborhood = Neighborhood.objects.create(neighborhood="Test Neighborhood")
        self.gender = Gender.objects.create(gender="Male")
        self.cribroom = Cribroom.objects.create(name="Test Cribroom")
        self.shift = Shift.objects.create(name="Morning Shift")

        # Eliminar el usuario si ya existe con la misma dirección de correo electrónico
        UserAccount.objects.filter(email="gogadicho@gmail.com").delete()

        self.user = UserAccount.objects.create_user(
            email="gogadicho@gmail.com",
            password="gogadicho",
            first_name="goga",
            last_name="chuch"
        )

        self.guardian = Guardian.objects.create(first_name="Guardian First Name", last_name="Guardian Last Name")
        self.child_state = ChildState.objects.create(name="Active")

        self.child = Child.objects.create(
            first_name="John",
            last_name="Doe",
            dni="12345678",
            birthdate="2000-01-01",
            street="Test Street",
            house_number=123,
            registration_date="2023-01-01",
            disenroll_date="2023-08-01",
            locality=self.locality,
            neighborhood=self.neighborhood,
            gender=self.gender,
            cribroom=self.cribroom,
            shift=self.shift,
            user=self.user,
            guardian=self.guardian,
            child_state=self.child_state
        )

    def test_child_str_method(self):
        expected_str = f"{self.child.last_name}, {self.child.first_name}"
        self.assertEqual(str(self.child), expected_str)

if __name__ == '__main__':
    unittest.main()
    