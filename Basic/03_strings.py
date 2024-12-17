### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) #9
print(len(my_other_string)) #14
print(my_string + " " + my_other_string) #Mi String Mi otro String

my_new_line_string = "Este es un String\ncon salto de línea" 
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Sencillo
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) #Más seguro (aseguramos el tipo)
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) #Tradicional, más pesado. 
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #Interpolación: Más sencillo que el primero.

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a) #p
print(e) #o

# División

language_slice = language[1:3] #del 1 al 3 (no incluido)
print(language_slice) #yt

language_slice = language[1:] #del 1 hasta el final
print(language_slice) #ython

language_slice = language[-2] #empezamos por el final
print(language_slice) #o

language_slice = language[0:6:2] #de 0 a 6 , de 2 en 2. Es decir: de la p a la n: p, t, o
print(language_slice) #pto

# Reverse

reversed_language = language[::-1]
print(reversed_language) #nohtyp

# Funciones del lenguaje

print(language.capitalize()) #Python
print(language.upper()) #PYTHON
print(language.count("t")) #1
print(language.isnumeric()) #False
print("1".isnumeric()) #True
print(language.lower()) #python
print(language.lower().isupper()) #False
print(language.startswith("Py")) #False
print("Py" == "py")  # False 