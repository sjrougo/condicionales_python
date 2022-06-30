# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

from queue import PriorityQueue


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print("Ingrese tres palabras, cada una seguida de un enter:")
palabra1 = str(input())
palabra2 = str(input())
palabra3 = str(input())
print("Escoja una forma de ordenamiento: \n1 para orden alfabetico \n2 para orden por longitud de palabras")
opcion = int(input())

if opcion == 1: #Controla si el usuario elige opción de ordenamiento alfabético
    if (palabra1<palabra2) and palabra1<palabra3:
        if palabra2<palabra3: #En línea 47 verífica si palabra1 es mayor a las otras dos, y luego ingresa y hace el control solo entre esas dos
            print("El orden es el siguiente: ", palabra1, palabra2, palabra3)
        else:
            print("El orden es el siguiente: ", palabra1, palabra3, palabra2)
    elif (palabra2<palabra1) and palabra2<palabra3:
        if palabra1<palabra3: #Si palabra1 no es mayor que las otras dos, pregunta si palabra2 es mayor a ambas, y luego controla solamente las mismas
            print("El orden es el siguiente: ", palabra2, palabra1, palabra3)
        else:
            print("El orden es el siguiente: ", palabra2, palabra3, palabra1)
    elif palabra3<palabra1 and palabra3<palabra2:
        if palabra1<palabra2: #Si palabra1 ni palabra2 son mayores, hace el mismo control para palabra3
            print("El orden el es siguiente: ", palabra3, palabra1, palabra2)
        else:
            print("El orden es el siguiente: ", palabra3, palabra2, palabra1)
elif opcion == 2: #Verifica si el usuario elige ordenamiento por longitud de palabras
    if len(palabra1)>len(palabra2) and len(palabra1)>len(palabra3):
        if len(palabra2)>len(palabra3):
            print("El orden es el siguiente: ", palabra1, palabra2, palabra3)
        else:
            print("El orden es el siguiente: ", palabra1, palabra3, palabra2)
    elif len(palabra2)>len(palabra1) and len(palabra2)>len(palabra3):
        if len(palabra1)>len(palabra3):
            print("El orden es el siguiente: ", palabra2, palabra1, palabra3)
        else:
            print("El orden es el siguiente: ", palabra2, palabra3, palabra1)
    elif len(palabra3)>len(palabra1) and len(palabra3)>len(palabra2):
        if len(palabra1)>len(palabra2):
            print("El orden el es siguiente: ", palabra3, palabra1, palabra2)
        else:
            print("El orden es el siguiente: ", palabra3, palabra2, palabra1)
else:
    print ("Debe ingresar una opción correcta")
