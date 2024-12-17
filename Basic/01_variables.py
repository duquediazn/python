#Usa snake_case:
my_string_variable = "My String variable"
my_int_variable = 5
my_bool_variable = False

print(my_string_variable) #My String variable
print(my_int_variable) #5
print(my_bool_variable) #False

#Concatenación de variables en un print
print(my_bool_variable, my_int_variable, my_string_variable) #False 5 My String variable
print(type(print(my_bool_variable, my_int_variable, my_string_variable))) #<class 'NoneType'>
print("Este es el valor de: ", my_bool_variable) #Este es el valor de:  False

#Funciones del sistema
print(len(my_string_variable)) #18
print(type(str(my_int_variable))) #<class 'str'>

#Variables en una sola línea: ¡Cuidado con abusar de esta sintaxis! 
name, surname, alias, age = "Nazaret", "Duque", "duquediazn", 36
print("Me llamo:", name, surname, ". Mi edad es: ", age, ". Y mi alias es: ", alias) #Me llamo: Nazaret Duque . Mi edad es:  36 . Y mi alias es:  duquediazn

#Inputs: 
#name = input("¿Cuál es tu nombre?")
#age = input("¿Cuántos años tienes")

print(name)
print(age)

#Tipado dinámico
name = 36
age = "Nazaret"
print(name) #36
print(age) #Nazaret

#Pero, ¿podemos forzar el tipado?
address: str = "Mi dirección" #A esto se le llama "anotación de tipo"
address = 32
print(type(address)) #<class 'int'>
"""
Respuesta: Not really :(
Podemos anotar el tipo para indicar una preferencia de tipado, pero no existe el tipado estático fuerte.
Las anotaciones de tipo, combinadas con herramientas como mypy o bibliotecas como pydantic, permiten acercarse 
al tipado fuerte
"""

