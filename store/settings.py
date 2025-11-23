import os
import logging

from pathlib import Path
from datetime import timedelta


from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shop",
    "cart",
    "pages",
    "users",
    "api",
    "social_django",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "store.middleware.request_timer.RequestTimerMiddleWare",
]


AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=100),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
}

LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname} {asctime} {message}]",
            "style": "{",
        }
    },
    "handlers": {},
    "loggers": {},
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("GOOGLE_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("GOOGLE_SECRET_KEY")
SOCIAL_AUTH_URL_NAMESPACE = "social"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

logger = logging.getLogger("social")
logger.setLevel(logging.DEBUG)

ROOT_URLCONF = "store.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR), "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "store.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


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


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}] {asctime} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "django_file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "django.log"),
            "formatter": "simple",
        },
        "app_file": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIR, "app.log"),
            "formatter": "simple",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["django_file", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["django_file", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["django_file", "console"],
            "level": "WARNING",
            "propagate": False,
        },
        "api": {
            "handlers": ["app_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
