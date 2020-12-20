from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "up-iaz)(u5s0l1z5%(kz(i3_v-v+3*k28$!)osoj$%!xd$r)j!"  # nosec development key
)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]  # nosec development hosts

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

try:
    from .local import *
except ImportError:
    pass
