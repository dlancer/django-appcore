from django.conf import settings

ANONYMOUS_REQUIRED_REDIRECT_URL = getattr(settings, 'ANONYMOUS_REQUIRED_REDIRECT_URL', '/')
