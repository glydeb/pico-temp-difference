import network
import socket
from time import sleep
import machine
import config

ssid = config.wifi_ssid
password = config.wifi_password

def connect_wifi():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print('changes implemented')
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print('Connection successful')
    print(wlan.ifconfig())

    return wlan

