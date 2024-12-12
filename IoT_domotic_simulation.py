
import sys
import json
import paho.mqtt.client
import re

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/luces/#', qos=2)
	client.subscribe(topic='casa/cortinas/#', qos=2)

def on_message(client, userdata, message):
	# * extraer la informacion del mensaje
	decoded=message.payload.decode('utf-8')
	msg_info=custom_json_parser(decoded)

	print('------------------------------')
	print('tema: %s' % message.topic)
	print('Valor: %s' % msg_info["value"])
	print('Precisiòn: %s' % msg_info["accuracy"])
	if msg_info['value']< 50 and  msg_info['accuracy']>0.9:
		print('Luces Encendidas')
	else:
		print('Luces Apagadas')

def main():
	client = paho.mqtt.client.Client(client_id='Daniel_domotics', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=5600)
	client.loop_forever()

def custom_json_parser(text):
    # !reemplaza comillas simples por comillas dobles
    text = text.replace("'", '"')
    # !aumenta comillas dobles en las claves del texto
    text = re.sub(r'(\w+):', r'"\1":', text)  
    print(text)
	# !Convierte la cadena de texto a json
    return json.loads(text)

if __name__ == '__main__':
	main()

sys.exit(0)

# {
#     device_id: "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
#     event_time: 2025-06-12 14:07:46.580465000,
#     value: 60,
#     accuracy: 0.98
# }
