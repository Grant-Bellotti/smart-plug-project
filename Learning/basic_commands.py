import paho.mqtt.client as mqtt

# MQTT broker details
broker = "grantbellotti.com"
port = 1883
username = "grant"
password = "12345"
client_id = "DVES_%06X"  # Tasmota typically uses DVES_ as default client_id

# Define the MQTT client (callback_api_version should be set as a keyword argument)
client = mqtt.Client(client_id=client_id)

# Set username and password
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker, port)

# Publish the "ON" command to the Tasmota device
#ret = client.publish("cmnd/tasmota_switch/LedPower", "1")
ret = client.publish("cmnd/tasmota_switch/POWER", "toggle")
print(ret)

#print(client.publish("stat/tasmota_switch"))

# Disconnect after publishing the message
client.disconnect()

