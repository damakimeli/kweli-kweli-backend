from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-local-dev-only')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'sermons',
    'chapel',
    'college',
    'prayers',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kwelikweli.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]

WSGI_APPLICATION = 'kwelikweli.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:admin123@localhost:5432/kwelikweli_db'
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12,
}

CORS_ALLOW_ALL_ORIGINS = True
JAZZMIN_SETTINGS = {
  "site_title": "Kweli Kweli Admin",
    "site_header": "Kweli Kweli Backend",
    "site_brand": "Kweli Kweli Portal",
    "welcome_sign": "Welcome to the Kweli Kweli Management System",
    "search_model": ["sermons.Sermon", "chapel.Chapel"],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "sermons.Sermon": "fas fa-video",
        "chapel.Chapel": "fas fa-church",
        "college.College": "fas fa-graduation-cap",
        "prayers.Prayer": "fas fa-hands-assembled"
    },
    # This turns on the live color customizer gear icon on your dashboard!
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
   "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    
    # Color Themes
    "theme": "simplex",                       # Vibrant, clean theme with striking red/dark accents
    "dark_mode_theme": None,
    
    # Component Styling
    "brand_colour": "navbar-danger",          # Bold brand color background for the top left logo area
    "navbar": "navbar-dark bg-dark",          # Sleek, professional jet-black top navbar
    "sidebar": "sidebar-dark-danger",         # Dark sidebar with rich red highlights matching active sections
    "accent": "accent-danger",                # Active links and form focus rings use the primary accent
    
    # Layout configuration
    "navbar_fixed": True,
    "side_nav_fixed": True,
    "no_navbar_border": True,
    "sidebar_nav_child_indent": True,
    
    # Make buttons big, bright, and impossible to miss!
    "button_classes": {
        "primary": "btn-danger shadow-sm font-weight-bold",   # Primary "Save" buttons turn into bold, vibrant red action items
        "secondary": "btn-outline-secondary",                 # Subtle outline for back/cancel buttons
        "info": "btn-info text-white",                        # Clear bright blue for informational triggers
        "warning": "btn-warning text-dark",                   # Warm gold for change/history items
        "danger": "btn-dark text-danger border-danger",       # Menacing dark border for deletes
        "success": "btn-success font-weight-bold"             # Vibrant green for add/create buttons
    }
}