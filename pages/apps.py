from django.apps import AppConfig


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

# settings
# pages.apps.PagesConfig pages -> apps.py -> class PagesConfig