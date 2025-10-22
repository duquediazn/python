### Variables ###

# Usa snake_case:
my_string_variable = "My String variable"
my_int_variable = 5
my_bool_variable = False

print(my_string_variable) #My String variable
print(my_int_variable) #5
print(my_bool_variable) #False

# Concatenación de variables en un print
print(my_bool_variable, my_int_variable, my_string_variable) #False 5 My String variable
print(type(print(my_bool_variable, my_int_variable, my_string_variable))) #<class 'NoneType'>
print("Este es el valor de: ", my_bool_variable) #Este es el valor de:  False

# Funciones del sistema
print(len(my_string_variable)) #18
print(type(str(my_int_variable))) #<class 'str'>

# Variables en una sola línea: ¡Cuidado con abusar de esta sintaxis! 
name, surname, alias, age = "Nazaret", "Duque", "duquediazn", 36
print("Me llamo:", name, surname, ". Mi edad es: ", age, ". Y mi alias es: ", alias) #Me llamo: Nazaret Duque . Mi edad es:  36 . Y mi alias es:  duquediazn

# Inputs: 
# name = input("¿Cuál es tu nombre?")
# age = input("¿Cuántos años tienes")

print(name)
print(age)

# Tipado dinámico
name = 36
age = "Nazaret"
print(name) #36
print(age) #Nazaret

# Anotación de tipo
address: str = "Mi dirección" 
address = 32
print(type(address)) #<class 'int'>

# En python no se pueden crear constantes como tal.
# Sin embargo, se pueden implementar constantes utilizando convenciones y buenas prácticas.
# Ejemplos:
'''
# En el módulo const.py:
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458
MAX_USERS = 100

# En el archivo principal:
import const

print(const.GRAVITY)  # 9.8
print(const.SPEED_OF_LIGHT)  # 299792458
print(const.MAX_USERS)  # 100
'''
