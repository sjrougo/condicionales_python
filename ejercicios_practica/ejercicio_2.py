# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if (texto_1>texto_2):
    print("La primer palabra es mayor alfabéticamente")
elif (texto_2>texto_1):
    print("La segunda palabra es mayor alfabéticamente")
else:
    print("Las palabras ingresadas son iguales.")


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
longitud_texto1 = len(texto_1)
longitud_texto2 = len(texto_2)
if (longitud_texto1>longitud_texto2):
    print("La palabra más larga es: ", texto_1)
elif (longitud_texto1<longitud_texto2):
    print("La palabra más larga es: ", texto_2)
else:
    print("La longitud de las palabras es la misma")


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
letra1 = texto_1[0]
letra2 = texto_2[0]
if letra1>letra2:
    print("La inicial de la primer palabra es mayor alfabeticamente")
elif letra1<letra2:
    print("La inicial de la segunda palabra es mayor alfabeticamente")
else:
    print("Las iniciales de ambas palabras son iguales")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1==texto_1:
    print ("Copia_texto1 y texto1 son iguales")
else:
    print("Copia_texto1 y texto1 son distintos")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1==texto_2:
    print ("Copia_texto1 y texto2 son iguales")
else:
    print("Copia_texto1 y texto2 no son iguales")
