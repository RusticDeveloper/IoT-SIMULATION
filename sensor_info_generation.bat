@echo off
:: Intervalo en segundos
set INTERVALO=2

:inicio
:: Generar un valor aleatorio entre 0 y 1
::set /a VALOR=!RANDOM! %% (%MAX% - %MIN% + 1) + %MIN%
SET /A VALOR=%RANDOM% * 100 / 32768 + 1
set /A INT_PART=%RANDOM% * 1000 / 32768

:: Insertar el punto decimal manualmente
set FLOAT_NUM=0.%INT_PART%

:: Mostrar el valor
echo Valor aleatorio (entre 1 y 100): %VALOR%
echo Valor aleatorio (entre 0 y 1): %FLOAT_NUM%
:: ejecutar la llamada
cd C:\program files\mosquitto
mosquitto_pub -h 127.0.0.1 -p 5600 -t "casa/luces/cocina" -m "{ deviceId:'5ee9df8-ff5fd3', eventTime:'2024-06-12 dfdsf', value:%VALOR%, accuracy:%FLOAT_NUM% }"

echo Presiona Ctrl+C para salir o espera el proximo valor.

:: Esperar el intervalo especificado
timeout /t %INTERVALO% >nul

:: Repetir el proceso
goto inicio