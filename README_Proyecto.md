# Proyecto: Procesador de Transacciones Bancarias

## Introducción

Este proyecto es una aplicación de línea de comandos (CLI) escrita en Python que procesa un archivo CSV con transacciones bancarias y genera un reporte. El reporte incluye:

- **Balance Final**: La diferencia entre los montos de las transacciones de tipo "Crédito" y "Débito".
- **Transacción de Mayor Monto**: El ID y el monto de la transacción con el valor más alto.
- **Conteo de Transacciones**: El número total de transacciones de tipo "Crédito" y "Débito".

El objetivo es proporcionar una herramienta simple para procesar y analizar transacciones bancarias almacenadas en archivos CSV.

## Instrucciones de Ejecución

### Requisitos
- Python 3.x
- El módulo `argparse` (para la lectura de parámetros desde la línea de comandos) y el módulo `csv` (para la lectura y procesamiento de archivos CSV) son parte de la biblioteca estándar de Python.

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/procesador_transacciones.git
