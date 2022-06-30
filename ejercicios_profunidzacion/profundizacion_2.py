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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print("Ingrese tres números enteros, cada uno seguido de un enter:")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

if (numero1%2)==0:
    print("El primer número es par")
else:
    print("El primer número es impar")

if (numero2%2)==0:
    print("El segundo número es par")
else:
    print("El segundo número es impar")

if (numero3%2)==0:
    print("El tercer número es par")
else:
    print("El tercer número es impar")
