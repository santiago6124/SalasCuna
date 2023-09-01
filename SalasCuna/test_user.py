import unittest


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

class Testuser(unittest.TestCase):

    def test_userAccount(self):
        useraccount = UserAccount.objects.create_user(
            email='ronaldihi04@gmail.com',
            first_name='jogo',
            last_name='gaucho',
            dni='67668768',
            phone_number='2355223',
            city='cordoba',
            is_active=True,
            is_staff=False,
            is_superuser=True
        )
        
        assert useraccount.first_name == 'jogo'


if __name__ == '__main__':
    unittest.main()
    