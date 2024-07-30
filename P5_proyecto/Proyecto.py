# Realiza un juego del ahorcado con lo aprendido.
# utiliza las funciones ya proporcionadas.

#Comprueba si una letra existe en una cadena
def comprobar_letra_en_cadena(letra="",cadena=""):
    if cadena.find(letra)!=-1:
        return True
    else:
        return False

#Añade una letra a un arreglo si no existe en el arreglo
def añadir_letra_arreglo(letra="",arreglo=[]):
    if not(letra in arreglo):
        arreglo.append(letra)

#comprueba una letra en un arreglo, si lo contiene
#devolvera verdadero en caso contrario sera falso
def comprobar_letra_en_arreglo(letra="",arreglo=[]):
    if letra in arreglo:
        return True
    else:
        return False

#Ejemplos de las funciones
arreglo=["H","o,","l","a"]
cadena = "hola"
#comprueba si la letra a existe en la cadena
print("comprueba si la letra a existe en la cadena:",cadena)
print(comprobar_letra_en_cadena("a",cadena))

#comprueba si la letra a existe en el arreglo
print("comprueba si la letra b existe en el arreglo:",arreglo)
print(comprobar_letra_en_arreglo("b",arreglo))

#añade la letra al arreglo 
print("añade la letra b al arreglo:", arreglo)
añadir_letra_arreglo("b",arreglo)
print(arreglo)
