# Configuración inicial tipo Django para el sistema

BASE_DIR = "backend"

SECRET_KEY = "cambiar-por-una-clave-segura-en-produccion"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "core",
    "apps.projects",
    "apps.users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES_DIR = "backend/templates"
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = "backend/media"
STATICFILES_DIRS = ["backend/static"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "proyectos_db",
        "USER": "postgres",
        "PASSWORD": "cambiar_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}