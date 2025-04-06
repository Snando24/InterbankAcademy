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

1. **Clona este repositorio:**

   ```bash
    git clone https://github.com/Snando24/InterbankAcademy.git

2. **Navegamos al directorio del proyecto:**
    cd Interbank-Academy

### Ejecución

1. **Entrada de Datos:**  
    La aplicación deberá leer un archivo CSV. Ejemplo de contenido:
    ```
    id,tipo,monto
    1,Crédito,100.00
    2,Débito,50.00
    3,Crédito,200.00
    4,Débito,75.00
    5,Crédito,150.00
    ```
    id: Identificador único de la transacción.
    tipo: El tipo de transacción ("Crédito" o "Débito").
    monto: El monto de la transacción (número decimal).

2. **Comando de ejecución en el directorio del proyecto:**
    python main.py ruta_del_archivo.csv
    **Donde ruta_del_archivo.csv es la ruta al archivo CSV que contiene las transacciones bancarias.**
    
    **En este caso viene a ser data.csv que se encuentra dentro de la carpeta interbanck-academy-25**

    **Así que el comando a ejecutar seria:**
    python main.py .\interbank-academy-25\data.csv

3. **Salida del Programa:** 
    Reporte de Transacciones
    ---------------------------------------------
    Balance Final: $/10985.85
    Transacción de Mayor Monto: ID 222 - 499.69
    Conteo de Transacciones: Crédito: 508 Débito: 492
