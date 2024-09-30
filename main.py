import time, machine
from wlan import connect_wifi
from flash import flash_led
from message_callback import on_message
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

        def on_message(topic, msg):
            nonlocal hvac_mode
            if topic == b"climate/system_mode":
                hvac_mode = msg.decode()

    # Listen for a message on topic climate/system_mode
    mqtt_client.set_callback(on_message)
    mqtt_client.subscribe(b"climate/system_mode")
    hvac_mode = b'idle'

    while True:
        mqtt_client.check_msg()
        # when system is on, read sensors and publish delta_t
        if hvac_mode in [b'heating', b'cooling']:
            sensor_data = read_sensors.get_SAT_RAT()
            if sensor_data is None or sensor_data['SAT'] is None or sensor_data['RAT'] is None:
                continue
            mode_adjustment = -1 if hvac_mode == b'cooling' else 1
            delta_t = (sensor_data['SAT'] - sensor_data['RAT']) * mode_adjustment
            print(sensor_data)
            mqtt_client.publish(b"pico/delta_t", str(delta_t).encode())
        time.sleep(1)  # Add a small delay to avoid busy-waiting

if __name__ == "__main__":
    main()