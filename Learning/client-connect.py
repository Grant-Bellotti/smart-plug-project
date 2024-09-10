import paho.mqtt.client as mqtt
import time, sys

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        print('Successfully connected!')
    else:
        print(f'Bad connection, broker returned code {rc}.')
        client.bad_connection_flag = True

def on_disconnect(client, userdata, flags, rc=0):
    print(f'Disconnected flags: {flags}, Result code: {rc}, Client_id: {client}.')
    client.connected_flag = False
    client.bad_connection_flag = False

def on_log(client, userdata,level, buf):
    print(f'Log: {buf}.')

broker = "grantbellotti.com"
port = 1883
username = "grant"
password = "12345"

mqtt.Client.connected_flag = False
mqtt.Client.bad_connection_flag = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log

client.loop_start()

try:
    client.username_pw_set(username, password)
    client.connect(broker, port)
except:
    print(f'Unable to connect to broker {broker}.')
    sys.exit(1)

while not client.connected_flag and not client.bad_connection_flag:
    print('Waiting for connection.')
    time.sleep(1)
    if client.bad_connection_flag:
        client.loop_stop()
        sys.exit(1)

ret = client.publish("cmnd/tasmota_switch/POWER", "off")
print(f'Message sent, broker returned: {ret}.')

time.sleep(2)

client.loop_stop()
client.disconnect()