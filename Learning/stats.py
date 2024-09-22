import paho.mqtt.client as mqtt
import time, sys, logging

logging.basicConfig(level=logging.INFO)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.connected_flag = True
        logging.info('Successfully connected!')
    else:
        logging.info(f'Bad connection, broker returned code {reason_code}.')
        client.bad_connection_flag = True

def on_disconnect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        logging.info(f'Disconnected successfully! Result code: {reason_code}.')
        client.connected_flag = False
        client.bad_connection_flag = False
    else:
        logging.info(f'Error disconnecting, result code: {reason_code}.')

def on_message(client, userdata, message):
    topic = message.topic
    msgr = str(message.payload.decode('utf-8'))
    logging.info(f'Message recieved on {topic}: {msgr}')

broker = "grantbellotti.com"
port = 1883
username = "grant"
password = "12345"

mqtt.Client.connected_flag = False
mqtt.Client.bad_connection_flag = False

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.loop_start()

try:
    client.username_pw_set(username, password)
    client.connect(broker, port)
except:
    logging.info(f'Unable to connect to broker {broker}.')
    sys.exit(1)

while not client.connected_flag and not client.bad_connection_flag:
    logging.info('Waiting for connection.')
    time.sleep(2)
    if client.bad_connection_flag:
        client.loop_stop()
        sys.exit(1)

#client.subscribe("stat/tasmota_switch/POWER")
client.subscribe("stat/tasmota_switch/STATUS8")
client.subscribe("tele/tasmota_switch/SENSOR")

# Message is retained by true at end
#client.publish("cmnd/tasmota_switch/POWER", "toggle")
client.publish("cmnd/tasmota_switch/STATUS", "8")

"""
{"StatusSNS":{
	"Time":"2024-09-10T22:21:27",
	"ENERGY"{
		"TotalStartTime":"2024-09-09T01:47:26", 
        "Total":0.003,                             # Total energy used in kWh
        "Yesterday":0.000,                         # Energy used yesterday in kWh
        "Today":0.003,                             # Energy used today in kWh
        "Power":32,                                # Current power usage in watts
        "ApparentPower":54,                        # Apparent power in volt-amperes (VA)
        "ReactivePower":43,                        # Reactive power in VAR
        "Factor":0.59,                             # Power factor
        "Voltage":119,                             # Voltage in volts
        "Current":0.451                            # Current in amps
		}
	}
}
"""

#logging.info(f'Message sent, broker returned: {ret}.')

time.sleep(1)

client.loop_stop()
client.disconnect()