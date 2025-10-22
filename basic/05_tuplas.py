### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Nazaret", "Duque", "Nazaret")
my_other_tuple = (35, 60, 30)

print(my_tuple) # (35, 1.77, 'Brais', 'Moure', 'Brais')
print(type(my_tuple)) # <class 'tuple'>
 
# Acceso a elementos y búsqueda

print(my_tuple[0]) # 35
print(my_tuple[-1]) # Nazaret
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Nazaret")) # 2
print(my_tuple.index("Duque")) # 3
print(my_tuple.index("Nazaret")) # 2

# La tupla se diferencia de una lista en que sus elementos son inmutables:
# my_tuple[1] = 1.80 # 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple 
print(my_sum_tuple) # (35, 1.77, 'Nazaret', 'Duque', 'Nazaret', 35, 60, 30)

# Subtuplas

print(my_sum_tuple[3:6]) # ('Duque', 'Nazaret', 35)

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "DuqueDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple) # (35, 'Azul', 1.77, 'Nazaret', 'Duque', 'DuqueDev')
print(type(my_tuple)) # <class 'tuple'>

# Eliminación

# No se pueden eliminar sus elementos (son inmutables):
# del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

#Pero si se puede eliminar la tupla:
del my_tuple
# print(my_tuple) # NameError: name 'my_tuple' is not defined