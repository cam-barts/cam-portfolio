from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

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
    }
}


try:
    from .local import *
except ImportError:
    pass
