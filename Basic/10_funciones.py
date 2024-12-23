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


print_name(surname="Moure", name="Brais") #Podemos cambiar el orden si lo indicamos, como en php

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure")
print_name_with_default("Brais", "Moure", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios

'''
Argumentos Variables: 
    El asterisco (*) permite que la función acepte un número variable de argumentos. 
    Esto significa que puedes llamar a la función con cero, uno o más argumentos, y todos ellos se agruparán en una tupla.

Cómo funciona:
    Los argumentos proporcionados después del asterisco (*) se empaquetan en una tupla con el nombre 
    que aparece después del asterisco (texts en este caso). Dentro de la función, puedes trabajar con 
    esa tupla como lo harías con cualquier otra tupla en Python.
'''

def print_upper_texts(*texts):
    print(type(texts)) # <class 'tuple'>
    for text in texts: # Itera sobre cada elemento de la tupla 'texts'
        print(text.upper())  # Convierte cada texto en mayúsculas y lo imprime

print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")

'''
<class 'tuple'>
HOLA
PYTHON
MOUREDEV
<class 'tuple'>
HOLA
'''