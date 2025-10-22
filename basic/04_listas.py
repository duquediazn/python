### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list)) #0

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) #[35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) #7

my_other_list = [35, 1.77, "Nazaret", "Duque"] 

print(type(my_list)) #<class 'list'>
print(type(my_other_list)) #<class 'list'>

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30)) #coincidencias del valor 30, devuelve 2
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Duque")) # 3

age, height, name, surname = my_other_list #desestructuración
print(name) # Nazaret

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) # 35

# Concatenación

print(my_list + my_other_list) #[35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']
#print(my_list - my_other_list) #TypeError: unsupported operand type(s) for -: 'list' and 'list'

# Creación, inserción, actualización y eliminación

my_other_list.append("NazaDev") #inserta al final  
print(my_other_list) # [35, 1.77, 'Nazaret', 'Duque', 'NazaDev']

my_other_list.insert(1, "Rojo") #inserta en la posición 1, rueda lo demás  
print(my_other_list) # [35, 'Rojo', 1.77, 'Nazaret', 'Duque', 'NazaDev']

my_other_list[1] = "Azul" #actualiza el valor en la posición 1  
print(my_other_list) # [35, 'Azul', 1.77, 'Nazaret', 'Duque', 'NazaDev']

my_other_list.remove("Azul") #elimina el valor "Azul"  
print(my_other_list) # [35, 1.77, 'Nazaret', 'Duque', 'NazaDev']

my_list.remove(30) #elimina el primer valor 30  
print(my_list) # [35, 24, 62, 52, 30, 17]

print(my_list.pop()) #elimina el último elemento de la lista  
print(my_list) # [35, 24, 62, 52, 30]

my_pop_element = my_list.pop(2) #elimina el elemento en la posición 2 y lo devuelve  
print(my_pop_element)  # 62
print(my_list) # [35, 24, 52, 30]

del my_list[2] #elimina el elemento en la posición 2, sin devolverlo  
print(my_list) # [35, 24, 30]

# Operaciones con listas

my_new_list = my_list.copy()

print(my_new_list == my_list) # True

my_list.clear() #reinicializar lista (vaciar)
print("ese",my_list) # []
print(my_new_list) # [35, 24, 30]

my_new_list.reverse() #revertir orden
print(my_new_list) # [30, 24, 35]

my_new_list.sort() #ordenar lista (de menor a mayor)
print(my_new_list) # [24, 30, 35]

# Sublistas

print(my_new_list[1:3]) #Muestra del 1 al 2 

# Cambio de tipo :(

my_list = "Hola Python"
print(my_list) # Hola Python
print(type(my_list)) # <class 'str'>

# Búsqueda

print(my_new_list.index(35)) #2
print(35 in my_new_list) #True