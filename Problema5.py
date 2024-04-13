# Problema 5

def Guardar_Tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 13):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"La tabla de multiplicar del {numero} se ha guardado en tabla-{numero}.txt")
    except IOError:
        print("Error al guardar la tabla de multiplicar.")

def Mostrar_Tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            tabla = archivo.read()
            print(f"Tabla de multiplicar del {numero}:\n{tabla}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def Mostrar_Linea_Tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if linea <= len(lineas):
                print(f"Línea {linea} de la tabla de multiplicar del {numero}: {lineas[linea - 1]}")
            else:
                print(f"La tabla de multiplicar del {numero} no tiene una línea {linea}.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\n*** Menú ***")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                Guardar_Tabla(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                Mostrar_Tabla(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea ver: "))
            if 1 <= numero <= 10 and 1 <= linea <= 10:
                Mostrar_Linea_Tabla(numero, linea)
            else:
                print("Los números deben estar entre 1 y 10.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
