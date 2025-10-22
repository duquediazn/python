### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'>
print(type(my_other_set))  # <class 'dict'> Inicialmente es un diccionario

my_other_set = {"Nazaret", "Duque", 35}
print(type(my_other_set)) # <class 'set'> Vuelve a ser un conjunto

print(len(my_other_set)) # 3

# Inserción

my_other_set.add("DuqueDev")

print(my_other_set)  # {'Nazaret', 'Duque', 35, 'DuqueDev'} Un set no es una estructura ordenada (hash)

my_other_set.add("DuqueDev")  # Un set no admite repetidos

print(my_other_set) # {'Nazaret', 'Duque', 35, 'DuqueDev'}

# Búsqueda

print("Duque" in my_other_set) # True
print("Duqui" in my_other_set) # False

# Eliminación

my_other_set.remove("Duque")
print(my_other_set) # {'Nazaret', 35, 'DuqueDev'}

my_other_set.clear()
print(len(my_other_set)) # 0

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Nazaret", "Duque", 35}
my_list = list(my_set)
print(my_list) # ['Nazaret', 'Duque', 35]
print(my_list[0]) # Nazaret

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # {35, 'Python', 'Swift', 'C#', 'Nazaret', 'Duque', 'JavaScript', 'Kotlin'}
print(my_set) # {'Nazaret', 'Duque', 35}
print(my_new_set) # {35, 'Python', 'Swift', 'Nazaret', 'Duque', 'Kotlin'}
print(my_new_set.difference(my_set)) # {'Python', 'Swift', 'Kotlin'} Devuelve los elementos de my_new_set que no están en my_set