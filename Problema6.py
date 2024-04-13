# Problema 6

import os

def Contar_Codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith('.py') or not os.path.exists(ruta_archivo):
            raise ValueError("La ruta especificada no es un archivo Python(.py) válido.")
        
        with open(ruta_archivo, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1
        return lineas_codigo
    
    except ValueError as e:
        print(e)
        return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    lineas_codigo = Contar_Codigo(ruta_archivo)
    if lineas_codigo is not None:
        print(f"El archivo tiene {lineas_codigo} líneas de código (excluyendo comentarios y líneas en blanco).")

if __name__ == "__main__":
    main()
