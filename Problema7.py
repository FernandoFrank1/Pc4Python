# Problema 7
 
import requests
import sqlite3
import time

def obtener_tipo_cambio(year, month):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?year={year}&month={month}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"Error al obtener el tipo de cambio para el año {year} y mes {month}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

def crear_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                            fecha TEXT PRIMARY KEY,
                            compra REAL,
                            venta REAL
                          )''')
        conn.commit()
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)

def verificar_tabla_vacia(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM sunat_info''')
        count = cursor.fetchone()[0]
        return count == 0
    except sqlite3.Error as e:
        print("Error al verificar la tabla:", e)
        return False

def insertar_datos(conn, data):
    try:
        cursor = conn.cursor()
        for registro in data:
            fecha = registro['fecha']
            compra = registro['compra']
            venta = registro['venta']
            cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) 
                              VALUES (?, ?, ?)''', (fecha, compra, venta))
        conn.commit()
    except sqlite3.Error as e:
        print("Error al insertar datos:", e)

def insertar_datos_en_archivo(data):
    try:
        if verificar_tabla_vacia(conn):
            with open('sunat_info.txt', mode='w') as file:
                for registro in data:
                    fecha = registro['fecha']
                    compra = registro['compra']
                    venta = registro['venta']
                    file.writelines([f'====== {fecha} =======\n', f'Compra USD: {compra}\n', f'Venta USD: {venta}\n'])
    except IOError as e:
        print("Error al escribir en el archivo:", e)

def mostrar_tabla(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM sunat_info''')
        rows = cursor.fetchall()
        for row in rows:
            fecha = row[0]
            compra = row[1]
            venta = row[2]
            print(f'====== {fecha} =======')
            print(f'Compra USD: {compra}')
            print(f'Venta USD: {venta}\n')
    except sqlite3.Error as e:
        print("Error al mostrar la tabla:", e)

def main():
    conn = sqlite3.connect('base.db')
    crear_tabla(conn)
    
    if verificar_tabla_vacia(conn): 
        for month in range(1, 13): 
            data = obtener_tipo_cambio(2023, month)
            if data:
                insertar_datos(conn, data)
            time.sleep(1) 
    else:
        print("La tabla 'sunat_info' ya contiene datos. No se insertarán nuevos registros.")
    
    print("Contenido de la tabla 'sunat_info':")
    mostrar_tabla(conn)
    
    conn.close()

if __name__ == "__main__":
    main()








