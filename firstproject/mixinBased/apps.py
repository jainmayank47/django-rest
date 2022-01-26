from django.apps import AppConfig


class MixinbasedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mixinBased'
