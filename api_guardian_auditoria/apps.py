from django.apps import AppConfig


class ApiGuardianAuditoriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_guardian_auditoria'
    def ready(self):
        import api_guardian_auditoria.signals