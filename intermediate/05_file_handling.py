### File Handling ###

import xml
import csv
import json
import os

# .txt file 
'''
# The old way
# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+") # Por defecto es "r". https://www.tutorialspoint.com/python/python_files_io.htm 

txt_file.write(
    "Mi nombre es Nazaret\nMi apellido es Duque\n36 años\nY mi lenguaje preferido es Python") # El puntero se quedará al final del archivo.

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
'''

# Alternativa para evitar el uso de "seek" y tener un código portable:

# Abrir en modo "w+" para escribir y leer
with open("Intermediate/my_file.txt", "w+") as txt_file:
    txt_file.write(
        "Mi nombre es Nazaret\nMi apellido es Duque\n35 años\nY mi lenguaje preferido es Python")

# Reabrir para lectura
with open("Intermediate/my_file.txt", "r") as txt_file: 
    for line in txt_file.readlines():
        print(line)

# Reabrir para agregar contenido al final
with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nAunque también me gusta Kotlin\nY Swift")

txt_file.close() # Cerramos recurso


# .json file

json_file = open("Intermediate/my_file.json", "w+") #Si no existe, lo crea

json_test = { # diccionario
    "name": "Nazaret",
    "surname": "Duque",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://Duque.dev"}

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
csv_writer.writerow(["Nazaret", "Duque", 35, "Python", "https://Duque.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?
# Usando el módulo xml.etree.ElementTree (más fácil)
import xml.etree.ElementTree as ET

# Crear la estructura del XML
root = ET.Element("data")

person = ET.SubElement(root, "person")
ET.SubElement(person, "name").text = "Nazaret"
ET.SubElement(person, "surname").text = "Duque"
ET.SubElement(person, "age").text = "35"
ET.SubElement(person, "language").text = "Python"

# Guardar el archivo XML
tree = ET.ElementTree(root)
with open("Intermediate/my_file.xml", "wb") as xml_file:
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)

# Leer el archivo XML
tree = ET.parse("Intermediate/my_file.xml")
root = tree.getroot()

for person in root.findall("person"):
    name = person.find("name").text
    surname = person.find("surname").text
    age = person.find("age").text
    language = person.find("language").text

    print(f"Nombre: {name}, Apellido: {surname}, Edad: {age}, Lenguaje: {language}")

"""
# Si buscas un XML visualmente más ordenado, minidom es una buena opción
import xml.dom.minidom as minidom

# Crear un documento XML
doc = minidom.Document()

# Elemento raíz
root = doc.createElement("data")
doc.appendChild(root)

# Crear un elemento 'person'
person = doc.createElement("person")
root.appendChild(person)

# Agregar subelementos con texto
name = doc.createElement("name")
name.appendChild(doc.createTextNode("Nazaret"))
person.appendChild(name)

surname = doc.createElement("surname")
surname.appendChild(doc.createTextNode("Duque"))
person.appendChild(surname)

age = doc.createElement("age")
age.appendChild(doc.createTextNode("35"))
person.appendChild(age)

language = doc.createElement("language")
language.appendChild(doc.createTextNode("Python"))
person.appendChild(language)

# Guardar el XML en un archivo
with open("Intermediate/my_file.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(doc.toprettyxml(indent="  "))

# Leer el archivo XML
from xml.dom import minidom

doc = minidom.parse("Intermediate/my_file.xml")
persons = doc.getElementsByTagName("person")

for person in persons:
    name = person.getElementsByTagName("name")[0].firstChild.data
    surname = person.getElementsByTagName("surname")[0].firstChild.data
    age = person.getElementsByTagName("age")[0].firstChild.data
    language = person.getElementsByTagName("language")[0].firstChild.data

    print(f"Nombre: {name}, Apellido: {surname}, Edad: {age}, Lenguaje: {language}")
"""