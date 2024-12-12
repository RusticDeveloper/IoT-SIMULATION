# Como implementar la simulacion IoT
1. Descargue los archivos del repositorio
2. instalar python y la siguiente libreria 'pip install paho-mqtt'
3. instalar mosquitto de la siguiente dirección 'https://mosquitto.org/download/', utilize la versión correspondiente a su sistema operativo
## siguientes pasos para windows
* Ejecute el archivo de python situandose en la capeta IoT SIMULATION y abriendo un simbolo del sistema, finalmente introducir la siguiente linea ``` python IoT_domotic_simulation.py ```
* En otro simbolo del sistema, muevase a  "C:\Program Files\mosquitto" y ejecute el siguiente comando ``` mosquitto_sub -h 127.0.0.1 -p 5600 -t "casa/luces/#" -v ```, para subcribirse al canal de luces.
* Por ultimo abra el archivo sensor_info_generation.bat, para que empieze a simular datos del sensor

## siguientes  pasos para linux
* Ejecute el archivo de python situandose en la capeta IoT SIMULATION y abriendo una teminal en el la capeta IOT SIMULATION e introducir la siguiente linea ``` python IoT_domotic_simulation.py ```
* En otra terminal y ejecute el siguiente comando ``` mosquitto_sub -h 127.0.0.1 -p 5600 -t "casa/luces/#" -v ```, para subcribirse al canal de luces.
* Por ultimo abra el archivo sensor_info_generation.sh con ``` chmod +x sensor_info_generator.sh
./sensor_info_generator.sh ```, para que empieze a simular datos del sensor

informacion de la api sobre la libreria Paho-mqtt 
https://eclipse.dev/paho/files/paho.mqtt.python/html/client.html#paho.mqtt.client.Client.connect
