### File Handling ###

import xml
import csv
import json
import os

# .txt file 

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+") # Por derecto es "r". https://www.tutorialspoint.com/python/python_files_io.htm 

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python") # El puntero se quedará al final del archivo.

txt_file.seek(0) # Hay que reposicionar el puntero al inicio antes de leer.
# print(txt_file.read()) # Lee todo el archivo
print(txt_file.read(10)) # Lee los 10 primeros caracteres
print(txt_file.readline()) # Lee una línea
print(txt_file.readline())
for line in txt_file.readlines(): # Leemos el resto del archivo línea a línea
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline()) # No se mostrará esta última línea, ya que el puntero se mueve al final del archivo al utilizar write()

with open("Intermediate/my_file.txt", "a") as my_other_file: # "a": append
    my_other_file.write("\nY Swift")

txt_file.close() # Cerrar recurso (buenas prácticas)

#os.remove("Intermediate/my_file.txt") # Borrar archivo


# Alternativa para evitar el uso de "seek" y tener un código portable:
""" 
# Abrir en modo "w+" para escribir y leer
with open("Intermediate/my_file.txt", "w+") as txt_file:
    txt_file.write(
        "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# Reabrir para lectura
with open("Intermediate/my_file.txt", "r") as txt_file: 
    for line in txt_file.readlines():
        print(line)

# Reabrir para agregar contenido al final
with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nAunque también me gusta Kotlin\nY Swift")

txt_file.close() # Cerramos recurso

 """

# .json file

json_file = open("Intermediate/my_file.json", "w+")

json_test = { # diccionario
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_test, json_file, indent=2) # "Volcado" de un diccionario sobre un fichero .json. La indentación 2 es la más "legible"
 
json_file.close() # Debemos cerrar el recurso

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json")) # "Carga" desde un fichero .json a un diccionario
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?