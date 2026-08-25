from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuración de la aplicación principal del Sistema Empresarial."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Catálogo'
