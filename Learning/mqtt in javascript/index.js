/*
const { MQTTClient } = require('node-mqtt-client');

const mqttClient = new MQTTClient();
mqttClient.host = 'grantbellotti.com';
mqttClient.port = 8883;
mqttClient.hostProtocol = MQTTClient.Protocol.MQTTS;
mqttClient.certificateManager.loadCertificates(
  "./ca.crt",
  "./client.crt",
  "./client.key"
);


mqttClient.username = 'grant';
mqttClient.password = '12345';

mqttClient.connect();
*/

const mqtt = require('mqtt')

const protocol = 'mqtt'
const host = 'grantbellotti.com'
const port = '1883'
const clientId = `mqtt_${Math.random().toString(16).slice(3)}`

const connectUrl = `${protocol}://${host}:${port}`

const client = mqtt.connect(connectUrl, {
  clientId,
  clean: true,
  connectTimeout: 4000,
  username: 'grant',
  password: '12345',
  reconnectPeriod: 1000,
})

client.on('connect', () => {
  console.log('Connected')

  // Publish a message to the specified topic
  client.publish('cmnd/tasmota_switch/POWER', 'toggle', { qos: 0, retain: false }, (error) => {
    if (error) {
      console.error('Publish error:', error);
    } else {
      console.log('Message sent: cmnd/tasmota_switch/POWER toggle');
    }
  });
  
})