# Programa para mostrar el uso de operadores lógicos en Python

# Definición de variables
a = True
b = False

print("Uso de operadores lógicos:\n")

# Operador AND
print("a = ",a)
print("b = ",b)

print("\nOperador AND:")
print("a and b =", a and b)  # False, porque True AND False es False
print("a and a =", a and a)  # True, porque True AND True es True

# Operador OR
print("\nOperador OR:")
print("a or b =", a or b)  # True, porque True OR False es True
print("b or b =", b or b)  # False, porque False OR False es False

# Operador NOT
print("\nOperador NOT:")
print("not a =", not a)  # False, porque NOT True es False
print("not b =",not b)  # True, porque NOT False es True

