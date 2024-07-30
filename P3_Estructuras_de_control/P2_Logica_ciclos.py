# Estructura for
print("\nEjemplo de bucle for:")
for i in range(5):  # Itera de 0 a 4
    print(f"Iteración {i}")

# Estructura while
print("\nEjemplo de bucle while:")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

# Ejemplo de bucle for con listas
print("\nRecorrer una lista con un bucle for:")
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

# Ejemplo de bucle while con una lista
print("\nRecorrer una lista con un bucle while:")
index = 0
while index < len(colores):
    print(colores[index])
    index += 1

# Uso de break y continue
print("\nUso de break y continue:")
for i in range(10):
    if i == 5:
        break  # Salir del bucle cuando i es 5
    print(i)


