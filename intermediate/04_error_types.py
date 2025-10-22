### Error Types ###
from math import pi
import math

# SyntaxError (error de sintaxis, algo está mal escrito)
# print "¡Hola comunidad!" # Descomentar para Error
print("¡Hola comunidad!")

# NameError (error variable no definida)
language = "Spanish"  # Comentar para Error
print(language)

# IndexError (error índice fuera de rango)
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError (error no se encuentra el módulo)
# import maths # Descomentar para Error

# AttributeError (error en el atributo, no existe o está mal escrito)
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError (error en el nombre de la clave, no existe o está mal escrita)
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError (error de tipado)
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError (error en el import, no existe o está mal escrito)
# from math import PI # Descomentar para Error
print(pi)

# ValueError (error al intentar convertir el valor al tipo especificado)
#my_int = int("10 Años") # Descomentar para Error
my_int = int("10")  
print(type(my_int))

# ZeroDivisionError (error al dividir entre cero)
# print(4/0) # Descomentar para Error
print(4/2)