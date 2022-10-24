from email.policy import default
from django.apps import AppConfig


class MusicappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'musicapp'
