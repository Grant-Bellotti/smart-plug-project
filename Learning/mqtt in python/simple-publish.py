import paho.mqtt.client as mqtt
import time, sys, logging

logging.basicConfig(level=logging.INFO)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True
        logging.info('Successfully connected!')
    else:
        logging.info(f'Bad connection, broker returned code {rc}.')
        client.bad_connection_flag = True

def on_disconnect(client, userdata, flags, rc=0):
    logging.info(f'Disconnected flags: {flags}, Result code: {rc}, Client_id: {client}.')
    client.connected_flag = False
    client.bad_connection_flag = False

def on_log(client, userdata,level, buf):
    logging.info(f'Log: {buf}.')

def on_publish(client, userdata, mid):
    logging.info(f'In on_publish callback mid: {mid}.')

def on_subscribe(client, userdata, mid, granted_qos):
    logging.info('Subscribed.')

def on_message(client, userdata, message):
    topic = message.topic
    msgr = str(message.payload.decode('utf-8'))
    logging.info(f'Message recieved: {msgr}')

def reset():
    ret = client.publish('house/bulb1', "", 0, True)
    logging.info(f'Broker cleared with return: {ret}.')

broker = "grantbellotti.com"
port = 1883
username = "grant"
password = "12345"

mqtt.Client.connected_flag = False
mqtt.Client.bad_connection_flag = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_publish = on_publish
client.on_subscribe = on_subscribe
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
    time.sleep(1)
    if client.bad_connection_flag:
        client.loop_stop()
        sys.exit(1)

#client.subscribe('house/bulb1', 2)

# Message is retained by true at end
ret = client.publish("house/bulb1", "Test message 0", 0, True)
logging.info(f'Message sent, broker returned: {ret}.')

ret = client.publish("house/bulb1", "Test message 1", 1)
logging.info(f'Message sent, broker returned: {ret}.')

ret = client.publish("house/bulb1", "Test message 2", 2)
logging.info(f'Message sent, broker returned: {ret}.')

time.sleep(2)

client.subscribe('house/bulb1', 2)
reset() # Reset held messages in broker

time.sleep(5)

client.loop_stop()
client.disconnect()