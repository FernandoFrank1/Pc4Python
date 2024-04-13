# Problema 2

from pyfiglet import Figlet
import random

figlet = Figlet()
fuentes = figlet.getFonts()

def selec_fuente():
    return random.choice(fuentes)

def Nom_fuente():
    font_input = input("Ingrese el nombre de la fuente (deje en blanco para aleatoria): ").strip()
    return font_input

def Texto():
    return input("Ingrese el texto a imprimir: ")

def Colores():
    return input("Ingrese el código de color ANSI para el fondo (deje en blanco para el color predeterminado): ").strip()

def print_Texto(text, font, Color = None):
    if Color:
        figlet.setFont(font=font, justify='center', bg=Color)
    else:
        figlet.setFont(font=font, justify='center')  # Se establece solo el justificado del texto
    print(figlet.renderText(text))

def main():
    try:
        font_input = Nom_fuente()
        
        selected_font = selec_fuente() if not font_input or font_input not in fuentes else font_input
        
        text_input = Texto()

        bg_color_input = Colores()
        
        print_Texto(text_input, selected_font,bg_color_input )
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")

if __name__ == "__main__":
    main()




