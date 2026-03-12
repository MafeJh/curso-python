###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

import math
from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name = input("¿Cuál es tu nombre?\n")
city = input("¿En qué ciudad vives?\n")

print(f"Tu nombre es {name}")
print(f"Vives en {city}")


###------------------------------------------------------------------

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(f"El tipo de a es {type(a)}, El tipo de b es {type(b)}, El tipo de c es {type(c)}, El tipo de d es {type(d)}, El tipo de e es {type(e)}")  # int

###------------------------------------------------------------------

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print("int(\"12345\") =", int("12345"))  # Convierte la cadena "12345" a un entero
print("float(int(\"12345\")) =", float(int("12345")))  # Convierte el entero resultante a float
print("int(3.99) =", int(3.99))  # Convierte el float 3.99 a un entero, se trunca la parte decimal y el resultado es 3

###------------------------------------------------------------------

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

name = "Mafe JH"
age = 27
height = 1.56
print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros")

###------------------------------------------------------------------

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
Pi = math.pi
print("2. Redondea el número con round()")
print("round(Pi) =", round(Pi))  # Redondea el número Pi al entero más cercano
print("3. Haz la división entera entre el número que te salió y el número 2")
print("round(Pi) // 2 =", round(Pi) // 2)  # Realiza la división entera entre el número redondeado de Pi y el número 2
print("4. El resultado debería ser 1")
print("Resultado:", round(Pi) // 2)  # Muestra el resultado de la división entera, que debería ser 1
