from django.apps import AppConfig


class MqttConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt'

    def ready(self):
        try:
            from mqtt.models import CheckClient
            if not CheckClient.objects.filter().exists():
                CheckClient.objects.create(active=False)
        except:
            pass
        return super().ready()