### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"Nombre": "Nazaret",
                 "Apellido": "Duque", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Nazaret",
    "Apellido": "Duque",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
print(my_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77}

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

# Búsqueda

print(my_dict[1]) # 1.77 
print(my_dict["Nombre"]) # Nazaret

print("Duque" in my_dict) #False, busca por clave
print("Apellido" in my_dict) #True

# Inserción

my_dict["Calle"] = "Calle DuqueDev"
print(my_dict) # {'Nombre': 'Nazaret', 'Apellido': 'Duque', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77, 'Calle': 'Calle DuqueDev'}

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Pedro

# Eliminación

del my_dict["Calle"]
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'Duque', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77}

# Otras operaciones (tiene copy, clear, etc.). Algunas operaciones propias:

print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellido', 'Duque'), ('Edad', 35), ('Lenguajes', {'Swift', 'Python', 'Kotlin'}), (1, 1.77)]) Retorna todos los pares clave-valor
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print(my_dict.values()) # dict_values(['Pedro', 'Duque', 35, {'Swift', 'Python', 'Kotlin'}, 1.77])

my_list = ["Nombre", 1, "Piso"]

#dict.fromkeys(): Crea un diccionario nuevo sin valores (los establece a "None"), y como claves lo que se le pase como argumento.
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) 
print((my_new_dict)) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict) #Utiliza las claves de my_dict
print((my_new_dict)) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
my_new_dict = dict.fromkeys(my_dict, "DuqueDev") #Se le puede añadir otro argumento para establecer los valores a algo distinto a "None"
print((my_new_dict)) # {'Nombre': 'DuqueDev', 'Apellido': 'DuqueDev', 'Edad': 'DuqueDev', 'Lenguajes': 'DuqueDev', 1: 'DuqueDev'}

my_values = my_new_dict.values()
print(type(my_values)) #Ojo, diccionario de valores <class 'dict_values'>

print(my_new_dict.values()) # dict_values(['DuqueDev', 'DuqueDev', 'DuqueDev', 'DuqueDev', 'DuqueDev'])
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # ['DuqueDev']
print(tuple(my_new_dict)) #Convierte a tupla solo las claves ('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)
print(set(my_new_dict)) #Convierte a conjunto solo las claves {'Apellido', 1, 'Nombre', 'Edad', 'Lenguajes'}