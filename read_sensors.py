# Description: This file contains the function to read the temperature sensors
import machine, onewire, ds18x20, time
import config

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

def get_SAT_RAT():
  # Get sensor addresses
  roms = ds_sensor.scan()
  print('Found DS devices: ', roms)
  
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  RAT_tempC = ds_sensor.read_temp(config.rat_rom)
  RAT_tempF = RAT_tempC * 1.8 + 32 if RAT_tempC is not None else None

  ds_sensor.convert_temp()
  time.sleep_ms(750)
  SAT_tempC = ds_sensor.read_temp(config.sat_rom)
  SAT_tempF = SAT_tempC * 1.8 + 32 if SAT_tempC is not None else None

# Create a dictionary to store sensor data
  sensor_data = {'SAT': SAT_tempF, 'RAT': RAT_tempF}
  return sensor_data