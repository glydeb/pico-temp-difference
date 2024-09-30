import machine
import time

led_pin = machine.Pin("LED", machine.Pin.OUT)

def flash_led(duration, interval):
    num_flashes = int(duration / interval)
    print(f"Flashing LED for {duration} seconds with an interval of {interval} seconds")
    
    for _ in range(num_flashes):
        led_pin.on()
        time.sleep(interval)
        led_pin.off()
        time.sleep(interval)
    return

# example usage
# while True:
#     try:    
#         flash_led(10, 0.5)
#         time.sleep(1)
#     except KeyboardInterrupt:
#         break 