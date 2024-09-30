import time, machine
from wlan import connect_wifi
from flash import flash_led
import read_sensors
import umqtt.simple
import mqtt



def main():
    # Connect to WiFi
    try:
        wifi = connect_wifi()
    except KeyboardInterrupt:
        machine.reset()
    except Exception as e:
        print(e)

    # Connect to MQTT broker

    # Check if connection is successful
    try:
        mqtt_client = mqtt.connect_mqtt()  
    except Exception as e:
        time.sleep(60)
        print(e)

    # Listen for a message on topic climate/system_mode
    hvac_mode = b'idle'

    def on_message(topic, message):
        # Perform desired actions based on the subscribed topic and response
        print('Received message on topic:', topic)
        print('Response:', message)
        nonlocal hvac_mode
        hvac_mode = message.decode()

    mqtt_client.set_callback(on_message)
    mqtt_client.subscribe(b"climate/system_mode")

    while True:
        mqtt_client.check_msg()
        print(hvac_mode)
        # when system is on, read sensors and publish delta_t
        if hvac_mode in ['heating', 'cooling']:
            sensor_data = read_sensors.get_SAT_RAT()
            if sensor_data is None or sensor_data['SAT'] is None or sensor_data['RAT'] is None:
                continue
            mode_adjustment = -1 if hvac_mode == b'cooling' else 1
            delta_t = (sensor_data['SAT'] - sensor_data['RAT']) * mode_adjustment
            print(sensor_data)
            mqtt_client.publish(b"pico/delta_t", str(delta_t).encode())
        time.sleep(10)  # Add a small delay to avoid busy-waiting

if __name__ == "__main__":
    main()