### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional O_O
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

# For

#for <variable> in <iterable>:
#    <Código>

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Nazaret", "Duque", "Nazaret")

for element in my_tuple:
    print(element)

my_set = {"Nazaret", "Duque", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Nazaret", "Apellido": "Duque", "Edad": 35, 1: "Python"}

for element in my_dict:
    print(element) #Imprime las keys, no los values. Para imprimir los valores, iteramos sobre my_dict.values()
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta") #Se lo salta si se cumple la condición.
else: #Opcional como en while
    print("El bluce for para diccionario ha finalizado")

# For en un rango numérico:
#range(inicio, fin, salto)

for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4

for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

# For en un string:

for i in "Python":
    print(i)

# Salida:
# P
# y
# t
# h
# o
# n

# For anidados

lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]

for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3

# Modificar elementos en listas, sets, diccionarios, etc: 

# Listas: 
numeros = [1, 2, 3, 4, 5]

for i in range(len(numeros)):  
    numeros[i] *= 2  # Multiplicamos cada número por 2

print(numeros)  # [2, 4, 6, 8, 10]

# O bien: 
numeros = [1, 2, 3, 4, 5]

for i, num in enumerate(numeros):
    numeros[i] = num * 2

print(numeros)  # [2, 4, 6, 8, 10]

'''
- enumerate(numeros) devuelve pares (índice, valor) de cada elemento en la lista.
- i representa la posición (índice) del elemento.
- num representa el valor en esa posición.
'''

# Diccionarios: 
edades = {"Juan": 20, "Ana": 25, "Luis": 30}

for key in edades:
    edades[key] += 1  # Incrementamos la edad en 1

print(edades)  # {'Juan': 21, 'Ana': 26, 'Luis': 31}

# Conjuntos (list comprehension): 
numeros = {1, 2, 3, 4, 5}
numeros_modificados = {num * 2 for num in numeros}  

print(numeros_modificados)  # {2, 4, 6, 8, 10}

# Tupla (de forma indirecta):
tupla = (1, 2, 3, 4, 5)
tupla_modificada = tuple(num * 2 for num in tupla)

print(tupla_modificada)  # (2, 4, 6, 8, 10)
