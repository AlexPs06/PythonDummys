# Realiza un juego del ahorcado con lo aprendido.
# utiliza las funciones ya proporcionadas.

import os

def limpiar_pantalla():
    """Limpia la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_ahorcado(vidas):
    # Lista de estados del ahorcado, desde 0 vidas (completo) hasta todas las vidas (sin dibujo).
    estados = [
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """
    ]
    # Imprime el estado correspondiente al número de vidas.
    print(estados[vidas])


def mostrar_progreso(palabra, letras_adivinadas):
    """Muestra los renglones con las letras adivinadas."""
    progreso = ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    print("\nPalabra:", progreso)

def juego_ahorcado(palabra_secreta):
    """Función principal del juego."""
    vidas = 6
    letras_adivinadas = set()
    intentos_fallidos = set()
    palabra_secreta = palabra_secreta.lower()
    
    while vidas > 0:
        limpiar_pantalla()
        imprimir_ahorcado(vidas)
        mostrar_progreso(palabra_secreta, letras_adivinadas)
        
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades, adivinaste la palabra!")
            break

        print("\nLetras incorrectas:", ', '.join(intentos_fallidos))
        print("Vidas restantes:", vidas)
        
        letra = input("\nIngresa una letra: ").lower()
        if len(letra) != 1:
            print("Por favor, ingresa solo una letra.")
            input("Presiona Enter para continuar...")
            continue

        if letra in letras_adivinadas or letra in intentos_fallidos:
            print("Ya intentaste esa letra.")
            input("Presiona Enter para continuar...")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.add(letra)
            print("¡Bien hecho!")
        else:
            intentos_fallidos.add(letra)
            vidas -= 1
            print("Letra incorrecta.")
        
        input("Presiona Enter para continuar...")

    if vidas == 0:
        limpiar_pantalla()
        imprimir_ahorcado(0)
        print("\nPerdiste. La palabra era:", palabra_secreta)

# Ejecución del juego
if __name__ == "__main__":
    palabra = input("Establece la palabra secreta: ")
    limpiar_pantalla()
    juego_ahorcado(palabra)