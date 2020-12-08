from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = [os.environ.get("DJANGO_HOST", "127.0.0.1")]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SECRET_KEY = os.environ["SECRET_KEY"]

INSTALLED_APPS = INSTALLED_APPS + [
    "storages",
]
# Static Stuff

DEFAULT_FILE_STORAGE = "portfolio.backend.AzureMediaStorage"
STATICFILES_STORAGE = "portfolio.backend.AzureStaticStorage"

AZURE_STORAGE_KEY = os.environ.get("AZURE_STORAGE_KEY", False)
AZURE_ACCOUNT_NAME = os.environ.get(
    "AZURE_STORAGE_NAME", "wagtailportfolio"
)  # your account name
AZURE_MEDIA_CONTAINER = os.environ.get("AZURE_MEDIA_CONTAINER", "media")
AZURE_STATIC_CONTAINER = os.environ.get("AZURE_STATIC_CONTAINER", "static")

AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.azureedge.net"  # CDN URL
# AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'  # Files URL

STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/"
MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/"

# DBHOST is only the server name, not the full URL
hostname = os.environ["DBHOST"]

# Configure Postgres database; the full username is username@servername,
# which we construct using the DBHOST value.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DBNAME"],
        "HOST": hostname + ".postgres.database.azure.com",
        "USER": os.environ["DBUSER"] + "@" + hostname,
        "PASSWORD": os.environ["DBPASS"],
        "PORT": "5432",
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}


try:
    from .local import *
except ImportError:
    pass
