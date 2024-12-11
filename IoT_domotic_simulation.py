
import sys
import json
import paho.mqtt.client

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/cocina/nevera', qos=2)

def on_message(client, userdata, message):
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	# * exxtraer la informacion del menaje
	msg_info=json.loads(message.payload)
	print('payload_value: %s' % msg_info["value"])
	print('qos: %d' % message.qos)

def main():
	client = paho.mqtt.client.Client(client_id='Daniel_domotics', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=5600)
	client.loop_forever()

if __name__ == '__main__':
	main()

sys.exit(0)

# {
#     device_id: "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
#     event_time: 2025-06-12 14:07:46.580465000,
#     value: 60,
#     accuracy: 0.98
# }
