import requests
import sqlite3
from datetime import datetime

def Precio_Bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        bitcoin_prices = {
            'USD': float(data['bpi']['USD']['rate'].replace(',', '')),
            'GBP': float(data['bpi']['GBP']['rate'].replace(',', '')),
            'EUR': float(data['bpi']['EUR']['rate'].replace(',', ''))
        }
        return bitcoin_prices
    except requests.RequestException as e:
        print("Error al conectar con la API de CoinDesk:", e)
        return None

def obtener_tipo_cambio(year, month):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?year={year}&month={month}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            tipo_cambio = float(data[0].get('Compra', 0))
            return tipo_cambio
        else:
            print("Los datos de la API de SUNAT no son válidos.")
            return None
    except requests.exceptions.HTTPError as e:
        print(f"Error al obtener el tipo de cambio para el año {year} y mes {month}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

def crear_tabla_bitcoin(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                            fecha TEXT PRIMARY KEY,
                            precio_usd REAL,
                            precio_gbp REAL,
                            precio_eur REAL,
                            precio_pen REAL
                          )''')
        conn.commit()
    except sqlite3.Error as e:
        print("Error al crear la tabla 'bitcoin':", e)

def insertar_datos_bitcoin(conn, bitcoin_prices, precio_pen):
    try:
        cursor = conn.cursor()
        fecha = datetime.now().strftime('%Y-%m-%d')
        cursor.execute('''INSERT OR IGNORE INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) 
                          VALUES (?, ?, ?, ?, ?)''', (fecha, bitcoin_prices['USD'], bitcoin_prices['GBP'], bitcoin_prices['EUR'], precio_pen))
        conn.commit()
    except sqlite3.Error as e:
        print("Error al insertar datos en la tabla 'bitcoin':", e)

def mostrar_datos_bitcoin(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM bitcoin''')
        rows = cursor.fetchall()
        for row in rows:
            print(f"Fecha: {row[0]}, Precio en USD: {row[1]}, Precio en GBP: {row[2]}, Precio en EUR: {row[3]}, Precio en PEN: {row[4]}")
    except sqlite3.Error as e:
        print("Error al mostrar los datos de la tabla 'bitcoin':", e)

def main():
    conn = sqlite3.connect('base.db')
    bitcoin_prices = Precio_Bitcoin()
    
    if bitcoin_prices is not None:
        tipo_cambio_pen = obtener_tipo_cambio(datetime.now().year, datetime.now().month)
        if tipo_cambio_pen is not None:
            crear_tabla_bitcoin(conn)
            insertar_datos_bitcoin(conn, bitcoin_prices, tipo_cambio_pen)
            print("Datos de precios de Bitcoin insertados correctamente en la tabla 'bitcoin'.")
            print("Datos de precios de Bitcoin:")
            mostrar_datos_bitcoin(conn)
        else:
            print("No se pudo obtener el tipo de cambio PEN desde la API de SUNAT.")
    else:
        print("No se pudieron obtener los precios de Bitcoin desde la API de CoinDesk.")
    
    conn.close()

if __name__ == "__main__":
    main()






