# Problema 3

import requests
import zipfile
from io import BytesIO
import os

URL = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

zip_file_name = "imagen.zip"

def Descarga_imagen(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
            zip_file.writestr("imagen.jpg", response.content)
        print("La imagen ha sido descargada y guardada en el archivo zip correctamente.")
    else:
        print("Error al descargar la imagen.")

def unzip_file(zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        zip_ref.extractall("unzipped_image")
    print("El archivo zip ha sido descomprimido correctamente.")

def main():
    Descarga_imagen(URL)
    
    unzip_file(zip_file_name)

if __name__ == "__main__":
    main()
