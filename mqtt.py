from time import sleep
from umqtt.simple import MQTTClient
import config

# Constants for MQTT Topics
MQTT_TOPIC_COIL_DELTA = 'pico/coil/delta'

# MQTT Parameters
MQTT_SERVER = config.mqtt_server
MQTT_PORT = 1883
MQTT_USER = config.mqtt_username
MQTT_PASSWORD = config.mqtt_password
MQTT_CLIENT_ID = b"raspberrypi_picow_1"
MQTT_KEEPALIVE = 7200
MQTT_SSL = False
MQTT_SSL_PARAMS = {'server_hostname': MQTT_SERVER}



def connect_mqtt():
    try:
        client = MQTTClient(client_id=MQTT_CLIENT_ID,
                            server=MQTT_SERVER,
                            port=MQTT_PORT,
                            user=MQTT_USER,
                            password=MQTT_PASSWORD,
                            keepalive=MQTT_KEEPALIVE,
                            ssl=MQTT_SSL,
                            ssl_params=MQTT_SSL_PARAMS)
        client.connect()
        return client
    except Exception as e:
        print('Error connecting to MQTT:', e)
        raise  # Re-raise the exception to see the full traceback

def publish_mqtt(client, topic, value):
    result = client.publish(topic, value)
    print(topic)
    print(value)
    print("Publish Done")
    return result

