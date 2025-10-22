### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) #floor division -> 3
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?") #concatenación de strings
# print("Hola " + 5) #¡Esto da error!: TypeError: can only concatenate str (not "int") to str
print("Hola " + str(5))

# Operaciones mixtas (con enteros)
print("Hola " * 5) #Hola Hola Hola Hola Hola
print("Hola " * (2 ** 3)) #Hola Hola Hola Hola Hola Hola Hola Hola

my_float = 2.5 * 2
print("Hola " * int(my_float)) #Hola Hola Hola Hola Hola

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print(3 == "3") #False, también compara tipado.

# Operaciones con cadenas de texto
print("Hola" > "Python") #F
print("Hola" < "Python") #T
print("aaaa" >= "abaa")  #F: Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  #T: Cuenta caracteres
print("Hola" <= "Python") #T
print("Hola" == "Hola") #T
print("Hola" != "Python") #T

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python") #F
print(3 > 4 or "Hola" > "Python") #F
print(3 < 4 and "Hola" < "Python") #T
print(3 < 4 or "Hola" > "Python") #T 
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) #T
print(not (3 > 4)) #T



