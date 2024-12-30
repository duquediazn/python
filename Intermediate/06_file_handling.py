### File Handling ###

import xml
import csv
import json
import os

# .txt file 

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python") # En Windows el puntero se quedará al final del archivo.

txt_file.seek(0) # Trabajando en Windows hay que reposicionar el puntero al inicio antes de leer.
# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline()) # En Windows no se mostrará esta última línea, el puntero se mueve al final del archivo al utilizar write()

txt_file.close() # Cerrar recurso (buenas prácticas)

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Intermediate/my_file.txt") # Borrar archivo

