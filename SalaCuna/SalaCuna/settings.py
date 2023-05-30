from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5f-+9^y8sdrrxk!93+h)h7#5(h-#o8(ypykyjs-t764u3(7_0#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "confApp",
    "rest_framework",
    "djoser",
    'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist'
]

JAZZMIN_SETTINGS = {
    "copyright": "ITSVillada 7C [Proyecto Salas Cunas]",
    "welcome_sign": "Bienvenido a las Salas Cunas [AdminSite]",
    "show-sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "-", "url": ""},
        {
            "name": "Jazzmin",
            "url": "https://github.com/farridav/django-jazzmin",
            "new_window": True,
        },
        {"name": "-", "url": ""},
        {
            "name": "Repository",
            "url": "https://github.com/santiago6124/SalasCuna",
            "new_window": True,
        },
        {"name": "-", "url": ""},
        {"app": "confApp"},
    ],
    "icons": {
        "auth.user": "far fa-user",
        "auth.Group": "fas fa-users",
        "confApp.Addresses": "fas fa-font",
        "confApp.Answers": "fas fa-pen",
        "confApp.Children": "fas fa-baby",
        "confApp.ChildrenState": "fas fa-check",
        "confApp.Cribrooms": "far fa-building",
        "confApp.Departments": "fas fa-route",
        "confApp.Desinfections": "fas fa-soap",
        "confApp.Districts": "far fa-map",
        "confApp.Forms": "fas fa-info",
        "confApp.Genders": "fas fa-restroom",
        "confApp.GuardianPhones": "fas fa-phone",
        "confApp.Guardians": "fas fa-user-secret",
        "confApp.Localities": "fas fa-city",
        "confApp.Options": "far fa-clipboard",
        "confApp.Padrones": "fas fa-file-import",
        "confApp.Paynote": "fas fa-receipt",
        "confApp.Payouts": "fas fa-money-bill",
        "confApp.QuestionTypes": "fas fa-book",
        "confApp.Questions": "fas fa-question",
        "confApp.Roles": "fas fa-user-tie",
        "confApp.Shifts": "far fa-address-card",
        "confApp.UserEmails": "far fa-envelope",
        "confApp.Users": "fas fa-street-view",
        "confApp.Zones": "far fa-square",
    },
    "order_with_respect_to": [
        "auth.user",
        "confApp.Users",
        "confApp.UserEmails",
        "confApp.Roles",
        "confApp.Children",
        "confApp.ChildrenState",
        "confApp.Genders",
        "confApp.Guardians",
        "confApp.GuardianPhones",
        "confApp.Shifts",
        "confApp.Cribrooms",
        "confApp.Desinfections",
        "confApp.Zones",
        "confApp.Departments",
        "confApp.Localities",
        "confApp.Districts",
        "confApp.Addresses",
        "confApp.Forms",
        "confApp.Questions",
        "confApp.QuestionTypes",
        "confApp.Options",
        "confApp.Answers",
        "confApp.Padrones",
        "confApp.Payouts",
        "confApp.Paynotes",
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-cyan",
    "accent": "accent-teal",
    "navbar": "navbar-success navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-teal",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "cyborg",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}


MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SalaCuna.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'build')],  
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = "SalaCuna.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "SalasCunas",
        "USER": "bdi",
        "PASSWORD": "pepe1234",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# JWT Auth

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

#DJOSER Conf

DJOSER = {
    'LOGIN_FIELD' : 'email',
    'USER_CREATE_PASSWORD_RETYPE' : True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION' : True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' : True,
    'SEND_CONFIRMATION_EMAIL' : True,
    'SET_USERNAME_RETYPE' : True,
    'SET_PASSWORD_RETYPE' : True,
    'PASSWORD_RESET_CONFIRM_URL' : 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL' : 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL' : 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL' : True,
    'SERIALIZERS' : {
        'user_create' : 'SalaCuna.serializers.UserCreateSerializer',
        'user' : 'SalaCuna.serializers.UserCreateSerializer',
        'user_delete' : 'djoser.serializers.UserDeleteSerializer',
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user model for user management

AUTH_USER_MODEL = "confApp.UserAccount"

# Email configutation

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cuentas.sistemas.sc@gmail.com'
EMAIL_HOST_PASSWORD = 'fkyqnsrctntvrtmx'
EMAIL_USE_TLS = True