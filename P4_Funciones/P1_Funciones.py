# Definición de una función simple sin parámetros
def saludar():
    print("¡Hola! ¿Cómo estás?")

# Llamada a la función saludar
saludar()

# Definición de una función con parámetros
def saludar_persona(nombre):
    print("¡Hola,",nombre, "! ¿Cómo estás?")

# Llamada a la función saludar_persona con un argumento
saludar_persona("Juan")

# Definición de una función con múltiples parámetros
def sumar(a, b):
    return a + b

# Llamada a la función sumar con dos argumentos
resultado = sumar(5, 3)
print("La suma de 5 y 3 es:", resultado)

# Definición de una función con un valor por defecto para un parámetro
def saludar_persona_con_edad(nombre, edad=18):
    print("¡Hola,", nombre, "! Tienes", edad,"años.")

# Llamada a la función saludar_persona_con_edad con y sin el argumento de edad
saludar_persona_con_edad("Ana", 25)
saludar_persona_con_edad("Luis")


