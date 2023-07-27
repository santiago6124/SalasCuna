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
    "corsheaders",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
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
            "name": "Repository (Backend)",
            "url": "https://github.com/santiago6124/SalasCuna",
            "new_window": True,
        },
        {"name": "-", "url": ""},
        {
            "name": "Repository (Frontend)",
            "url": "https://github.com/santiago6124/SalasCuna-FE-",
            "new_window": True,
        },
        {"name": "-", "url": ""},
        {"app": "confApp"},
    ],
    "hide_apps": ["auth", "token_blacklist"],
    "icons": {
        "confApp.Adress": "fas fa-font",
        "confApp.Child": "fas fa-baby",
        "confApp.ChildState": "fas fa-check",
        "confApp.Company": "fas fa-landmark",
        "confApp.Cribroom": "far fa-building",
        "confApp.CribroomUser": "fas fa-vest",
        "confApp.Desinfection": "fas fa-soap",
        "confApp.Form": "fas fa-info",
        "confApp.Gender": "fas fa-restroom",
        "confApp.GuardianPhone": "fas fa-phone",
        "confApp.Guardian": "fas fa-user-secret",
        "confApp.Payout": "fas fa-money-bill",
        "confApp.Role": "fas fa-user-tie",
        "confApp.Shift": "far fa-address-card",
        "confApp.UserAccount": "fas fa-user-secret",
        "confApp.UserEmail": "far fa-envelope",
        "confApp.User": "fas fa-street-view",
        "confApp.Zone": "far fa-square",
    },
    "order_with_respect_to": [
        "confApp.UserAccount",
        "confApp.User",
        "confApp.UserEmail",
        "confApp.Role",
        "confApp.Child",
        "confApp.ChildState",
        "confApp.Gender",
        "confApp.Guardian",
        "confApp.GuardianPhone",
        "confApp.Shift",
        "confApp.Cribroom",
        "confApp.CribroomUser",
        "confApp.Desinfection",
        "confApp.Company",
        "confApp.Payout",
        "confApp.Zone",
        "confApp.Adress",
        "confApp.Form",
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
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "SalasCuna.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "build")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "SalasCuna.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

# JWT Authentication

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# JWT

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# DJOSER Configuration

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create": "SalasCuna.serializers.UserCreateSerializer",
        "user": "SalasCuna.serializers.UserCreateSerializer",
        "current_user": "SalasCuna.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user model for user management

AUTH_USER_MODEL = "confApp.UserAccount"

# Email configutation

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "cuentas.sistemas.sc@gmail.com"
EMAIL_HOST_PASSWORD = "fkyqnsrctntvrtmx"
EMAIL_USE_TLS = True

DOMAIN = "localhost:3000"
SITE_NAME = "Salas Cuna"

# Corsheaders configuration

CORS_ALLOW_ALL_ORIGINS = True
