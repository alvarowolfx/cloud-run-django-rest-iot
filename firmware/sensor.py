from hcsr04 import HCSR04
import machine
import network
import ubinascii
import utime as time
import urequests as requests

import config

sensor = HCSR04(trigger_pin=config.TRIGGER_PIN, echo_pin=config.ECHO_PIN)


def wifi_connect():
    """Connect to the configured Wi-Fi network."""
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print('network config:', sta_if.ifconfig())


def get_device_id():
    return ubinascii.hexlify(machine.unique_id()).decode('utf-8')


def get_distance():
    """Obtain the current distance measurement from the ultrasonic sensor.
    The returned distance is in centimeters.
    """
    return sensor.distance_cm()


def show_error():
    """Blink the ESP8266 LED a few times to indicate that an error has
    occurred.
    """
    led = machine.Pin(config.LED_PIN, machine.Pin.OUT)
    for i in range(5):
        time.sleep(0.5)
        led.on()
        time.sleep(0.5)
        led.off()
    led.on()


def send_data(data):
    """
    Send data to the backend.
    """
    data['device_id'] = get_device_id()
    print('sending: ', data)
    response = requests.post(config.URL, json=data)
    if response.status_code != 200:
        raise RuntimeError('Could not send data!')
    print('data sent!')


def deep_sleep():
    """Put the ESP8266 board into deep sleep mode for the configured length
    of time.
    At the end of the deep sleep period the board will reboot.
    """
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, config.INTERVAL * 1000)
    machine.deepsleep()
