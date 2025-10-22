### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Duque", name="Nazaret") #Podemos cambiar el orden si lo indicamos, como en php

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Nazaret", "Duque")
print_name_with_default("Nazaret", "Duque", "DuqueDev")

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts)) # <class 'tuple'>
    for text in texts: # Itera sobre cada elemento de la tupla 'texts'
        print(text.upper())  # Convierte cada texto en mayúsculas y lo imprime

print_upper_texts("Hola", "Python", "DuqueDev")
print_upper_texts("Hola")

'''
<class 'tuple'>
HOLA
PYTHON
DuqueDEV
<class 'tuple'>
HOLA
'''