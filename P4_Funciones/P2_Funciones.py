# Función para calcular el área de un círculo
def area_circulo(radio):
    pi = 3.14159
    return pi * radio * radio

# Función para calcular el perímetro de un círculo
def perimetro_circulo(radio):
    pi = 3.14159
    return 2 * pi * radio

# Uso de las funciones
radio = 5
print("El área de un círculo con radio", radio," es:", area_circulo(radio))
print("El perímetro de un círculo con radio", radio, "es:", perimetro_circulo(radio))
