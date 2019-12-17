"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# -----------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# -----------------------------------------------------------------------
DEBUG = os.getenv("APP_ENV") == "development"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATE_DIRS = (BASE_DIR, "../templates")
ROOT_URLCONF = "happiness.urls"
WSGI_APPLICATION = "happiness.wsgi.application"


# -----------------------------------------------------------------------
# Security
# -----------------------------------------------------------------------
# WARNING: keep the secret key used in production secret! ##
# -----------------------------------------------------------------------

# Allowed hosts to run the application on
ALLOWED_HOSTS = [".herokuapp.com", "localhost"]

# conditional for secret key depending on environment
if os.getenv("APP_ENV") == "production":
    SECRET_KEY = os.getenv("SECRET_KEY")
else:
    SECRET_KEY = ",^NqzcYF'#V3jh(NqvJZ*gm28&^4YE{C8?<78MCB{*z'XE?o]}"

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Ssl conditional local or Heroku
if os.getenv("APP_ENV") == "production":
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT")
else:
    SECURE_SSL_REDIRECT = False

# -----------------------------------------------------------------------
# Application Configuration
# -----------------------------------------------------------------------
# Django default
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Middleware Config
    # User apps
    "rating.apps.happiness",
]

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
            ]
        },
    }
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # ...
]


# -----------------------------------------------------------------------
# Database Configuration
# -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# -----------------------------------------------------------------------
if os.getenv("APP_ENV") == "production":
    DATABASES = {}
    DATABASES["default"] = dj_database_url.config(ssl_require=True)
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "happinessdb",
            "USER": "postgres",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "",
        }
    }


# -----------------------------------------------------------------------
# Internationalization
# -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# -----------------------------------------------------------------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# -----------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# -----------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# -----------------------------------------------------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
