import csv
import argparse

def parse_args():
    # Crear un analizador de argumentos
    parser = argparse.ArgumentParser(description="Procesar transacciones bancarias.")
    # Agregar un argumento para la ruta del archivo CSV
    parser.add_argument('archivo', type=str, help="Ruta del archivo CSV de transacciones.")
    return parser.parse_args()

def validar_transaccion(transaccion):
    try:
        monto = float(transaccion['monto'])
        if monto < 0:
            raise ValueError("El monto no puede ser negativo.")
    except ValueError as e:
        print(f"Error: {e}")
        return False

    if transaccion['tipo'] not in ['Crédito', 'Débito']:
        print("Error: Tipo de transacción inválido.")
        return False

    return True


def leer_csv(ruta_archivo):
    try:
        transacciones = []
        # Abre el archivo CSV en modo lectura
        # Usa encoding='utf-8' para evitar problemas con caracteres especiales
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # Crea un lector CSV
            # Usa DictReader para leer el archivo como un diccionario
            lector = csv.DictReader(archivo)
            for fila in lector:
                if len(fila) != 3:
                    print(f"Advertencia: Fila con número incorrecto de columnas detectada: {fila}")
                    continue  # Ignorar filas con más o menos columnas
                if not validar_transaccion(fila):
                    print(f"Transacción inválida: {fila}")
                    continue
                transacciones.append(fila)
        return transacciones
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{ruta_archivo}'. El programa finalizó.")
        exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit(1)

def procesar_transacciones(transacciones):
    balance_final = 0
    transaccion_mayor_monto = None # Inicializa como None para identificar la transacción de mayor monto como DICCIONARIO
    conteo_credito = 0
    conteo_debito = 0

    for transaccion in transacciones:
        monto = float(transaccion['monto'])
        tipo = transaccion['tipo']

        # Actualizar balance
        if tipo == "Crédito":
            balance_final += monto
            conteo_credito += 1
        elif tipo == "Débito":
            balance_final -= monto
            conteo_debito += 1

        # Identificar la transacción de mayor monto
        if transaccion_mayor_monto is None or monto > float(transaccion_mayor_monto['monto']):
            transaccion_mayor_monto = transaccion

    return balance_final, transaccion_mayor_monto, conteo_credito, conteo_debito

def mostrar_reporte(balance, transaccion_mayor_monto, conteo_credito, conteo_debito):
    
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: $/{balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {transaccion_mayor_monto['id']} - {transaccion_mayor_monto['monto']}")
    print(f"Conteo de Transacciones: Crédito: {conteo_credito} Débito: {conteo_debito}")

def main():
    # Llama a la función parse_args para obtener los argumentos de la línea de comandos
    args = parse_args()
    ruta_archivo = args.archivo
    transacciones = leer_csv(ruta_archivo)
    balance, transaccion_mayor_monto, conteo_credito, conteo_debito = procesar_transacciones(transacciones)
    mostrar_reporte(balance, transaccion_mayor_monto, conteo_credito, conteo_debito)

if __name__ == '__main__':
    main()
