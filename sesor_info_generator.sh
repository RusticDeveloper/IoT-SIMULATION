#!/bin/bash
# Intervalo en segundos
INTERVALO=5

# Bucle infinito
while true; do
    # Generar un valor aleatorio entre 0 y 1
    VALOR=$((RANDOM % (1 - 0 + 1) + MIN))
    # Generar un valor aleatorio entre 1 y 50
    VALOR1=$((RANDOM % (100 - 1 + 1) + MIN))
    echo "Presiona 'q' para salir o espera $INTERVALO segundos."
    # Mostrar el valor aleatorio
    echo "Valor aleatorio (entre 0 y 1): $VALOR"
    echo "Valor aleatorio (entre 0 y 1): $VALOR1"
    # Esperar entrada del usuario o tiempo
    read -t $INTERVALO -n 1 INPUT
    # Ejecutar la llamada al comando mosquitto_pub
    mosquitto_pub -h 127.0.0.1 -p 5600 -t "casa/luces/dormitorio" -m "{ deviceId:'5ee9df8-ff5fd3', eventTime:'2024-06-12 dfdsf', value:$VALOR, accuracy:$FLOAT_NUM }"
    # Si el usuario presiona 'q', salir del bucle
    if [ "$INPUT" == "q" ]; then
        echo "Saliendo del script..."
        break
    fi

    # Esperar el intervalo especificado
    sleep $INTERVALO
done
