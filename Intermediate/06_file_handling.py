### File Handling ###

# Nota: Moure trabaja en MacOS

import xml
import csv
import json
import os

# .txt file 

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python") # En Windows y Linux el puntero se quedará al final del archivo.

txt_file.seek(0) # Trabajando en Windows y Linux hay que reposicionar el puntero al inicio antes de leer.
# print(txt_file.read()) # Lee todo el archivo
print(txt_file.read(10)) # Lee los 10 primeros caracteres
print(txt_file.readline()) # Lee una línea
print(txt_file.readline())
for line in txt_file.readlines(): # Leemos el resto del archivo línea a línea
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline()) # En Windows no se mostrará esta última línea, el puntero se mueve al final del archivo al utilizar write()

txt_file.close() # Cerrar recurso (buenas prácticas)

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt") # Borrar archivo

""" 
# Alternativa para evitar el uso "seek" y tener un código portable:

# Abrir en modo "w+" para escribir y leer
with open("Intermediate/my_file.txt", "w+") as txt_file:
    txt_file.write(
        "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")
    txt_file.flush()  # Asegurar que los datos escritos estén sincronizados (importante en Windows)

# Reabrir para lectura
with open("Intermediate/my_file.txt", "r") as txt_file:
    print(txt_file.read(10))
    print(txt_file.readline())
    print(txt_file.readline())
    for line in txt_file.readlines():
        print(line)

# Reabrir para agregar contenido al final
with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nAunque también me gusta Kotlin")
    my_other_file.write("\nY Swift") 
"""
