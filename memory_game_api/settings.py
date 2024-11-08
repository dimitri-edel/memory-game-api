"""
Django settings for memory_game_api project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Import environment variables
if os.path.exists("/opt/gameapi2/memory-game-api/memory_game_api/env.py") or os.path.exists("memory_game_api/env.py"):
    print("Importing environment variables from env.py")
    from .env import *
else:
    print("Failed to import env.py!")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-l5pxf6qy$5jtk=si0pj#&qi@7r83j2xaz#)0mu(r14l1d8lmq1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "127.0.0.1:5500",
]

# If os.environ["DEPLOYED_HOSTNAME"] is set, add it to ALLOWED_HOSTS
if "DEPLOYED_HOSTNAME" in os.environ:
    ALLOWED_HOSTS.append(os.environ["DEPLOYED_HOSTNAME"])

ALLOWED_CLIENT_HOSTS = [
    "http://127.0.0.1:5500",
    "https://dimitri-edel.github.io",
]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "category",
    "playlist", 
    "quiz", 
    "face",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Allow all origins (for development purposes)
CORS_ALLOW_ALL_ORIGINS = True

# Alternatively, you can specify allowed origins
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:5500",
#     "http://localhost:5500",
# ]

# Allow specific headers
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "token1",
    "token2",
    # Add your custom headers here
    # Add other headers if needed
]

ROOT_URLCONF = "memory_game_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "memory_game_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.environ["DB_PORT"],
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Set this flag to True, when deploying to production
DEPLOYED = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

if not DEPLOYED:
    STATIC_URL = "static/"
else:
    STATIC_URL = "gameapi/static/"

# Media files settings
if not DEPLOYED:
    MEDIA_URL = '/media/'    
else:
    MEDIA_URL = 'gameapi/media/'
    MEDIA_ROOT = '/opt/gameapi2/memory-game-api/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# API Media Storage
API_MEDIA_STORAGE = "MEDIA_FOLDER"
