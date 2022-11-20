import network

import secret

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secret.SSID, secret.WIFI_PASSWORD)
print("Connecting to Xb-wifi_2.4G")

while not wlan.isconnected():
    pass

print("Connected to Xb-wifi_2.4G")
import urequests

r = urequests.get("https://www.google.com")
print(r.content)
