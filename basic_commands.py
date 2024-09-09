import paho.mqtt.client as mqtt

# MQTT broker details
broker = "grantbellotti.com"
port = 1883
username = "grant"
password = "12345"
client_id = "DVES_%06X"  # Tasmota typically uses DVES_ as default client_id
topic = "cmnd/tasmota_switch/POWER"  # Full topic for sending commands

# Define the MQTT client (callback_api_version should be set as a keyword argument)
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker, port)

# Publish the "ON" command to the Tasmota device
client.publish(topic, "OFF")

# Disconnect after publishing the message
client.disconnect()

print("ON command sent to the Tasmota plug")
