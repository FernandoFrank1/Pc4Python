# Problema 4

import requests
import csv

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except requests.RequestException:
        print("Error al conectar con la API de CoinDesk.")
        return None
    except KeyError:
        print("Error al procesar los datos recibidos.")
        return None

def guardar_datos_en_archivo(precio_bitcoin):
    if precio_bitcoin is None:
        return
    try:
        with open('precio_bitcoin.txt', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([precio_bitcoin])
        print("Datos guardados correctamente en el archivo precio_bitcoin.txt")
    except IOError:
        print("Error al abrir o escribir en el archivo.")

def main():
    precio_bitcoin = obtener_precio_bitcoin()
    guardar_datos_en_archivo(precio_bitcoin)

if __name__ == "__main__":
    main()
