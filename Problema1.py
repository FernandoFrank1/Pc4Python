# Problema 1

import requests

def Precio_Bitcoin():
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

def Calcula_Costo_Bitcoins(bitcoins, precio_bitcoin):
    if precio_bitcoin is None:
        return None
    return bitcoins * precio_bitcoin

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return

    precio_bitcoin = Precio_Bitcoin()
    if precio_bitcoin is not None:
        costo_en_usd = Calcula_Costo_Bitcoins(cantidad_bitcoins, precio_bitcoin)
        if costo_en_usd is not None:
            print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
