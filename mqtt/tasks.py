import json
import redis
import time

from random import uniform

from celery import shared_task
import paho.mqtt.client as mqtt

from mqtt.models import Log, WarningLog

from core.settings import (
    DES_MQTT,
    DES_REDIS,
    INPUT_CHANNEL,
    OUTPUT_CHANNEL,
    TOPIC,
    DES_MQTT_USERNAME,
    DES_MQTT_PASSWORD,
    DES_MQTT_PORT,
    DES_MQTT_CLIENT_ID,
    DES_REDIS_PASSWORD
)


r = redis.Redis(host=DES_REDIS, port=6379, password=DES_REDIS_PASSWORD)


def on_message(client, userdata, message):
    data = json.loads(message.payload.decode("utf-8"))
    Log.objects.create(**data)

    r.publish(channel=INPUT_CHANNEL, message=message.payload)


@shared_task
def start_subscriber():
    client = mqtt.Client(DES_MQTT_CLIENT_ID)
    client.username_pw_set(DES_MQTT_USERNAME, DES_MQTT_PASSWORD)
    client.connect(DES_MQTT, int(DES_MQTT_PORT))
    client.subscribe(TOPIC)
    client.loop_start()
    client.on_message = on_message


@shared_task
def get_warns():
    pubsub = r.pubsub()
    pubsub.subscribe(OUTPUT_CHANNEL)

    for message in pubsub.listen():
        if isinstance(message["data"], bytes):
            data = json.loads(message["data"])
            WarningLog.objects.create(**data)
