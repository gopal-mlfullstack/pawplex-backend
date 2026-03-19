import os
from datetime import timedelta
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

# 🔐 SECURITY
SECRET_KEY = env("SECRET_KEY")

DEBUG = False  # ✅ MUST be False in production

ALLOWED_HOSTS = [
    "gopalmahatobackend.pythonanywhere.com",
]

# 🌐 Applications
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "channels",
    "django_filters",
    "django_celery_beat",
    "django_celery_results",
    # your apps
    "accounts",
    "pets",
    "appointments",
    "adoption",
    "community",
    "emergency",
    "dashboard",
    "notifications",
]

# ⚙️ Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # CSRF (keep it)
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🌍 URLs
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# 🗄️ Database (SQLite ok for now)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔐 Auth
AUTH_USER_MODEL = "accounts.User"

# 🌐 DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# 🔑 JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# 📦 Static & Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 🌍 CORS (IMPORTANT)
CORS_ALLOWED_ORIGINS = [
    "https://petpluscare.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_HEADERS = True

# 🔐 CSRF (IMPORTANT for Netlify frontend)
CSRF_TRUSTED_ORIGINS = [
    "https://petpluscare.netlify.app",
]

# 🔒 Security headers (PRODUCTION BEST PRACTICE)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# (Optional but recommended if HTTPS always)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
