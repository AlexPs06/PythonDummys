# Ejemplo de estructuras de control en Python

# Estructura if, elif, else
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


# Ejemplo con operadores lógicos y condicionales
edad = int(input("\nIngrese su edad: "))
tiene_permiso = input("¿Tiene permiso de sus padres? (si/no): ").lower() == "si"

# Condición para permitir entrada a un evento
if edad >= 18 or (edad >= 16 and tiene_permiso):
    print("Puede entrar al evento.")
else:
    print("No puede entrar al evento.")