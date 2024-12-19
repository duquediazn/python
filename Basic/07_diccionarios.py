### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict) #False, busca por clave
print("Apellido" in my_dict) #True

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones (tiene copy, clear, etc.). Algunas operaciones propias:

print(my_dict.items()) #Retorna todos los pares clave-valor
print(my_dict.keys()) 
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

#dict.fromkeys(): Crea un diccionario nuevo sin valores (los establece a "None"), y como claves lo que se le pase como argumento.
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) 
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict) #Utiliza las claves de my_dict
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev") #Se le puede añadir otro argumento para establecer los valores a algo distinto a "None"
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values)) #Ojo, diccionario de valores <class 'dict_values'>

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict)) #Convierte a tupla solo las claves
print(set(my_new_dict)) #Convierte a conjunto solo las claves