from django.http import JsonResponse
from celery.result import AsyncResult

from mqtt.tasks import start_subscriber, get_warns
def start_mqtt_subscriber(request):
    task = start_subscriber.delay()
    get_warns.delay()

    return JsonResponse({'response': 'MQTT subscriber started', 'task_id': task.id})

def stop_mqtt_subscriber(request):
    task_id = request.GET.get("task_id")
    task = AsyncResult(task_id)
    task.revoke(terminate=True)

    return JsonResponse({'response': 'MQTT subscriber stopped'})