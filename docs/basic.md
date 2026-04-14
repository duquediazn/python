# Fundamentos de Python

---

## Índice

1. [Hola Mundo y variables](#hola-mundo-y-variables--volver-al-inicio)
2. [Operadores](#operadores-aritméticos--volver-al-inicio)
3. [Strings](#strings--volver-al-inicio)
4. [Estructuras de datos](#estructuras-de-datos--volver-al-inicio)
5. [Condicionales y bucles](#condicionales-y-bucles--volver-al-inicio)
6. [Funciones](#️funciones--volver-al-inicio)
7. [Clases y excepciones](#clases-y-excepciones--volver-al-inicio)
8. [Módulos](#módulos--volver-al-inicio)

---

## Hola Mundo y variables [🔝 Volver al inicio](#)

Imprimir por pantalla:

```python
print("Hola Python")
print('Hola Python')
```

### Comentarios en Python [🔝 Volver al inicio](#)

Comentario en una línea:

```python
# Esto es un comentario de una línea
```

Comentarios multilínea (triple comilla simple o doble):

```python

"""
Comentario
en varias
líneas
"""

'''
Este también es
un comentario
en varias líneas
'''
```

> 🔹 En realidad, Python no tiene una sintaxis específica para comentarios multilínea.  
> Estas cadenas se interpretan como **strings no asignados**, que el intérprete ignora.

### Tipos de datos básicos [🔝 Volver al inicio](#)

Para consultar el tipo de un dato se usa `type()`:

```python
print(type("Hola Python")) #<class 'str'>
print(type(5)) #<class 'int'>
print(type(5.2)) #<class 'float'>
print(type(True)) #<class 'bool'>
print(type(1+3j)) #<class 'complex'>
```

> 🔹 `complex` representa números complejos, poco comunes en uso general, pero útiles en matemáticas o física.

### Variables y nombres [🔝 Volver al inicio](#)

Para nombrar las variables se usa `snake_case`:

```python
my_string_variable = "My String variable"
my_int_variable = 5
my_bool_variable = False

print(my_string_variable) #My String variable
print(my_int_variable) #5
print(my_bool_variable) #False
```

### Concatenación y tipo de retorno en `print` [🔝 Volver al inicio](#)

```python
print(my_bool_variable, my_int_variable, my_string_variable) #False 5 My String variable
print(type(print(my_bool_variable, my_int_variable, my_string_variable))) #<class 'NoneType'>
print("Este es el valor de: ", my_bool_variable) #Este es el valor de:  False
```

> 🔹 `print()` siempre devuelve `None`, por eso su tipo es `NoneType`.

### Funciones del sistema [🔝 Volver al inicio](#)

```python
print(len(my_string_variable)) #18
print(type(str(my_int_variable))) #<class 'str'>
```

> 🔹 `len()` devuelve la longitud de un objeto iterable.  
> 🔹 `str()` convierte cualquier valor a cadena de texto.

### Asignación múltiple [🔝 Volver al inicio](#)

Variables en una sola línea (útil, pero no abusar):

```python
name, surname, alias, age = "Nazaret", "Duque", "duquediazn", 36
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)
```

### Entradas por teclado [🔝 Volver al inicio](#)

```python
name = input("¿Cuál es tu nombre?")
age = input("¿Cuántos años tienes?")

print(name)
print(age)
```

> 🔹 `input()` devuelve siempre una cadena de texto (`str`), incluso si el usuario escribe un número.

### Tipado dinámico y anotaciones de tipo [🔝 Volver al inicio](#)

```python
name = 36
age = "Nazaret"
print(name)
print(age)

address: str = "Mi dirección"
address = 32
print(type(address)) #<class 'int'>
```

> 🔹 Python es de **tipado dinámico y débil**: el tipo de una variable puede cambiar en tiempo de ejecución.  
> 🔹 Las **anotaciones de tipo** (`: str`, `: int`, etc.) son solo informativas. No imponen restricciones a nivel de intérprete.

### Constantes en Python [🔝 Volver al inicio](#)

Python no tiene constantes verdaderas.  
Por convención, se escriben en **mayúsculas** y se asume que no deben modificarse.

En el módulo `const.py`:

```python
GRAVITY = 9.8
SPEED_OF_LIGHT = 299792458
MAX_USERS = 100
```

En el archivo principal:

```python
import const
print(const.GRAVITY)  # 9.8
print(const.SPEED_OF_LIGHT)  # 299792458
print(const.MAX_USERS)  # 100
```

> 🔹 Si bien nada impide cambiar su valor, las mayúsculas sirven como aviso al programador.  
> 🔹 En proyectos grandes, se pueden usar herramientas de validación o convenciones de estilo (como `flake8` o `mypy`) para reforzar este comportamiento.

## ➕ Operadores [🔝 Volver al inicio](#)

### Operadores Aritméticos [🔝 Volver al inicio](#)

Operaciones con enteros:

```python
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3) #floor division -> 3
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)
```

Operaciones con cadenas de texto:

```python
print("Hola " + "Python " + "¿Qué tal?") #concatenación de strings
# print("Hola " + 5) #¡Esto da error!: TypeError: can only concatenate str (not "int") to str
print("Hola " + str(5))
```

Operaciones mixtas (con enteros)

```python
print("Hola " * 5) #Hola Hola Hola Hola Hola
print("Hola " * (2 ** 3)) #Hola Hola Hola Hola Hola Hola Hola Hola
my_float = 2.5 * 2
print("Hola " * int(my_float)) #Hola Hola Hola Hola Hola
```

### Operadores Comparativos [🔝 Volver al inicio](#)

Operaciones con enteros:

```python
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print(3 == "3") #False, también compara tipado.
```

Operaciones con cadenas de texto:

```python
print("Hola" > "Python") #F
print("Hola" < "Python") #T
print("aaaa" >= "abaa")  #F: Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  #T: Cuenta caracteres
print("Hola" <= "Python") #T
print("Hola" == "Hola") #T
print("Hola" != "Python") #T
```

### Operadores Lógicos [🔝 Volver al inicio](#)

Basada en el [Álgebra de Boole](https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole)

```python
print(3 > 4 and "Hola" > "Python") #F
print(3 > 4 or "Hola" > "Python") #F
print(3 < 4 and "Hola" < "Python") #T
print(3 < 4 or "Hola" > "Python") #T
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) #T
print(not (3 > 4)) #T
```

## Strings [🔝 Volver al inicio](#)

Los **strings** o cadenas de texto en Python se pueden definir con comillas simples `'` o dobles `"`.  
Ambas son equivalentes, pero se recomienda ser consistente dentro de un mismo proyecto.

```python
my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string)) #9
print(len(my_other_string)) #14
print(my_string + " " + my_other_string) #Mi String Mi otro String
```

> 🔹 `len()` devuelve la longitud (número de caracteres) de una cadena.  
> 🔹 El operador `+` concatena textos.

### Secuencias especiales [🔝 Volver al inicio](#)

Python reconoce ciertos **caracteres de escape** dentro de las cadenas:

```python
my_new_line_string = "Este es un String\ncon salto de línea"
my_tab_string = "\tEste es un String con tabulación"
my_scape_string = "\\tEste es un String \\n escapado"
```

> 🔹 `\n` genera un salto de línea.  
> 🔹 `\t` inserta una tabulación.  
> 🔹 Para mostrar el carácter `\` literalmente, se debe “escapar” con `\\`.

### Formateo de cadenas [🔝 Volver al inicio](#)

Existen múltiples formas de insertar variables dentro de un texto:

```python
name, surname, age = "Nazaret", "Duque", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
```

> 🔹 `.format()` es versátil y seguro.  
> 🔹 `%s`, `%d`, etc. es un método heredado del C, aún válido.  
> 🔹 La concatenación con `+` es más manual y menos eficiente.  
> 🔹 Las **f-strings** (`f"..."`) son la forma moderna y más legible.

### Desempaquetado de caracteres [🔝 Volver al inicio](#)

Una cadena es una **secuencia inmutable** de caracteres.  
Podemos asignar cada carácter a una variable:

```python
language = "python"
a, b, c, d, e, f = language
print(a) #p
print(e) #o
```

> 🔹 El desempaquetado funciona si el número de variables coincide con la longitud de la cadena.

### Slicing o división de cadenas [🔝 Volver al inicio](#)

Python permite acceder a partes de una cadena mediante índices:

```python
language = "python"
print(language[1:3])    # del 1 al 3 (sin incluir 3)
print(language[1:])     # del índice 1 hasta el final
print(language[-2])     # segundo carácter desde el final
print(language[0:6:2])  # de 0 a 6, saltando de 2 en 2
print(language[::-1])   # invertir la cadena
```

> 🔹 La sintaxis general es `cadena[inicio:fin:paso]`.

### Métodos comunes de strings [🔝 Volver al inicio](#)

Python incluye una gran cantidad de métodos útiles para manipular cadenas:

```python
language = "python"
print(language.capitalize()) #Python
print(language.upper()) #PYTHON
print(language.count("t")) #1.
print(language.isnumeric()) #False
print("1".isnumeric()) #True
print(language.lower()) #python
print(language.lower().isupper()) #False
print(language.startswith("Py")) #False
print("Py" == "py")  # False
print(sorted(language)) # ['h', 'n', 'o', 'p', 't', 'y']
print(len(language)) # 6
```

> 🔹 `capitalize()` → primera letra en mayúscula.  
> 🔹 `upper()` / `lower()` → cambia el caso.  
> 🔹 `count()` → cuenta ocurrencias.  
> 🔹 `startswith()` → comprueba prefijo.  
> 🔹 `sorted()` → devuelve lista con los caracteres ordenados. [sorted()](https://www.w3schools.com/python/ref_func_sorted.asp)
> 🔹 `isnumeric()` → determina si el texto representa un número.

### Otros métodos útiles [🔝 Volver al inicio](#)

```python
print("mambo".center(11,"#")) ###mambo###
print("mambo".find("a",0,len("mambo"))) # 1
print("mambo".index("a",0,len("mambo"))) # 1
print("Me gusta mucho el mambo, ¡soy el rey del mambo!".replace("mambo", "twerking")) # Me gusta mucho el twerking, ¡soy el rey del twerking!
print("Me gusta mucho el mambo, ¡soy el rey del mambo!".replace("mambo", "twerking", 1)) # Me gusta mucho el twerking, ¡soy el rey del mambo!
print('1,2,3'.split(',')) # ['1', '2', '3']
print('1,2,3'.split(',', maxsplit=1)) # ['1', '2,3']
print('   spacious   '.strip()) # 'spacious'
print('Hello world'.title()) # Hello World
```

> 🔹 `center(ancho, relleno)` → centra el texto.  
> 🔹 `find()` → devuelve el índice de la primera coincidencia o -1.  
> 🔹 `index()` → igual que `find()`, pero lanza un error si no hay coincidencia.  
> 🔹 `replace()` → reemplaza texto (opcionalmente limitado por número de ocurrencias).  
> 🔹 `split()` → divide una cadena en una lista.  
> 🔹 `strip()` → elimina espacios al inicio y final.  
> 🔹 `title()` → capitaliza cada palabra.

Más métodos: [Documentación oficial de cadenas](https://docs.python.org/3/library/stdtypes.html#string-methods)

> ⚠️ ¡Estos métodos no soportan expresiones regulares!

---

## Estructuras de datos [🔝 Volver al inicio](#)

### Listas [🔝 Volver al inicio](#)

Las **listas** en Python son estructuras de datos ordenadas y mutables que permiten almacenar múltiples elementos de cualquier tipo.

#### Definición

```python
my_list = list()
my_other_list = []

print(len(my_list)) #0

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list) #[35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) #7

my_other_list = [35, 1.77, "Nazaret", "Duque"]

print(type(my_list)) #<class 'list'>
print(type(my_other_list)) #<class 'list'>
```

> 🔹 Las listas pueden contener elementos de distintos tipos.  
> 🔹 `len()` devuelve el número de elementos.

#### Acceso a elementos y búsqueda [🔝 Volver al inicio](#)

```python
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
```

> 🔹 Los índices negativos cuentan desde el final de la lista.  
> 🔹 `count()` devuelve cuántas veces aparece un valor.  
> 🔹 `index()` devuelve la posición del primer elemento encontrado.  
> 🔹 También es posible desempaquetar listas en variables.

#### Concatenación de listas

```python
print(my_list + my_other_list)
# [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Nazaret', 'Duque']
# print(my_list - my_other_list)  # TypeError: unsupported operand type(s) for -: 'list' and 'list'
```

> 🔹 Las listas se pueden concatenar con `+`, pero no restar.

#### Creación, inserción, actualización y eliminación

```python
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
```

> 🔹 `append()` añade al final.  
> 🔹 `insert(pos, valor)` inserta en una posición concreta.  
> 🔹 `remove(valor)` elimina la primera coincidencia.  
> 🔹 `pop()` elimina y devuelve un elemento.  
> 🔹 `del` elimina sin devolver.

---

#### Operaciones con listas

```python
my_new_list = my_list.copy()

print(my_new_list == my_list) # True

my_list.clear() #reinicializar lista (vaciar)
print("ese",my_list) # []
print(my_new_list) # [35, 24, 30]

my_new_list.reverse() #revertir orden
print(my_new_list) # [30, 24, 35]

my_new_list.sort() #ordenar lista (de menor a mayor)
print(my_new_list) # [24, 30, 35]
```

> 🔹 `copy()` crea una copia independiente.  
> 🔹 `clear()` vacía la lista.  
> 🔹 `reverse()` invierte el orden.  
> 🔹 `sort()` ordena los elementos (solo si son comparables).

#### Sublistas (slicing)

```python
print(my_new_list[1:3]) #Muestra del 1 al 2
```

> 🔹 Igual que con strings, se usa la notación `[inicio:fin]` para obtener una sublista.

#### Cambio de tipo

```python
my_list = "Hola Python"
print(my_list) # Hola Python
print(type(my_list)) # <class 'str'>
```

> ⚠️ Cuidado: reasignar una lista a otro tipo deja inaccesible la estructura anterior.

#### Búsqueda

```python
print(my_new_list.index(35)) #2
print(35 in my_new_list) #True
```

> 🔹 `in` comprueba si un elemento está contenido en la lista (devuelve `True` o `False`).  
> 🔹 `index()` devuelve la posición del primer elemento coincidente.

#### Resumen

- Las listas son **mutables** (pueden modificarse).
- Permiten **duplicados** y **mezcla de tipos**.
- Soportan **slicing**, **búsqueda**, **inserción**, **ordenación** y **comprobación de pertenencia**.
- Son la estructura más usada en Python para colecciones ordenadas de datos.

---

### Tuplas [🔝 Volver al inicio](#)

Las **tuplas** en Python son estructuras de datos ordenadas e **inmutables**.  
Una vez creadas, **no se pueden modificar**, añadir ni eliminar elementos individuales.

#### Definición

```python
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Nazaret", "Duque", "Nazaret")
my_other_tuple = (35, 60, 30)

print(my_tuple) # (35, 1.77, 'Nazaret', 'Duque', 'Nazaret')
print(type(my_tuple)) # <class 'tuple'>
```

> 🔹 Las tuplas pueden contener diferentes tipos de datos, igual que las listas.  
> 🔹 Pueden incluir valores duplicados.  
> 🔹 Se definen con paréntesis `()` o usando el constructor `tuple()`.

#### Acceso a elementos y búsqueda

```python
print(my_tuple[0]) # 35
print(my_tuple[-1]) # Nazaret
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Nazaret")) # 2
print(my_tuple.index("Duque")) # 3
print(my_tuple.index("Nazaret")) # 2
```

> 🔹 Los índices funcionan igual que en las listas (positivos o negativos).  
> 🔹 `count()` devuelve el número de apariciones de un elemento.  
> 🔹 `index()` devuelve la posición del primer elemento encontrado.  
> 🔹 Si el elemento no existe, `index()` lanza un `ValueError`.

#### Inmutabilidad

```python
my_tuple[1] = 1.80 # 'tuple' object does not support item assignment
```

> ⚠️ A diferencia de las listas, **no se pueden modificar los elementos de una tupla**.  
> Intentar hacerlo genera un error `TypeError`.

#### Concatenación

```python
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # (35, 1.77, 'Nazaret', 'Duque', 'Nazaret', 35, 60, 30)
```

> 🔹 Puedes unir tuplas con el operador `+`.  
> 🔹 Esto crea una nueva tupla, ya que las existentes no se pueden alterar.

#### Subtuplas (slicing)

```python
print(my_sum_tuple[3:6]) # ('Duque', 'Nazaret', 35)
```

> 🔹 Igual que las listas, admiten **slicing** con la notación `[inicio:fin]`.

### Tupla mutable (conversión a lista)

```python
my_tuple = list(my_tuple)
print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "DuqueDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple) # (35, 'Azul', 1.77, 'Nazaret', 'Duque', 'DuqueDev')
print(type(my_tuple)) # <class 'tuple'>
```

> 🔹 Aunque una tupla es inmutable, se puede **convertir temporalmente en lista**, modificarla y volverla a convertir en tupla.  
> 🔹 Esta técnica es útil si necesitas editar o actualizar su contenido.

#### Eliminación

```python
del my_tuple[2] # TypeError: 'tuple' object doesn't support item deletion

del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined
```

> 🔹 No se pueden eliminar elementos individuales, pero sí eliminar la **tupla completa** con `del`.  
> 🔹 Esto borra la variable del espacio de memoria.

#### Resumen

- Las tuplas son **ordenadas e inmutables**.
- Se pueden **indexar, contar, concatenar y recorrer**, pero no modificar.
- Son más ligeras y seguras que las listas, ideales para datos constantes.
- Para editar su contenido, se pueden **convertir a lista** y luego de nuevo a tupla.

---

### Sets [🔝 Volver al inicio](#)

Los **sets** o **conjuntos** en Python son colecciones **no ordenadas**, **mutables** y **sin elementos duplicados**.  
Se basan en el concepto matemático de conjunto.

#### Definición

```python
my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'>
print(type(my_other_set))  # <class 'dict'> Inicialmente es un diccionario

my_other_set = {"Nazaret", "Duque", 35}
print(type(my_other_set)) # <class 'set'> Vuelve a ser un conjunto

print(len(my_other_set)) # 3
```

> 🔹 Los conjuntos se definen con llaves `{}` o con `set()`.  
> 🔹 Si se usa `{}` vacío, Python crea un **diccionario**, no un set.  
> 🔹 No admiten duplicados y su orden interno no está garantizado.

#### Inserción

```python
my_other_set.add("DuqueDev")
print(my_other_set)  # {'Nazaret', 'Duque', 35, 'DuqueDev'} Un set no es una estructura ordenada (hash)

my_other_set.add("DuqueDev")  # Un set no admite repetidos
print(my_other_set) # {'Nazaret', 'Duque', 35, 'DuqueDev'}
```

> 🔹 `add()` añade un nuevo elemento, pero **ignora duplicados**.  
> 🔹 El orden de los elementos puede cambiar al imprimir, ya que el set no mantiene orden.

#### Búsqueda

```python
print("Duque" in my_other_set) # True
print("Duqui" in my_other_set) # False
```

> 🔹 El operador `in` permite comprobar si un elemento pertenece al conjunto.  
> 🔹 Es muy eficiente, ya que los sets usan **tablas hash** para las búsquedas.

#### Eliminación

```python
my_other_set.remove("Duque")
print(my_other_set) # {'Nazaret', 35, 'DuqueDev'}

my_other_set.clear()
print(len(my_other_set)) # 0

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined
```

> 🔹 `remove()` elimina un elemento específico (lanza error si no existe).  
> 🔹 `clear()` vacía el conjunto.  
> 🔹 `del` elimina la variable por completo.

#### Transformación

```python
my_set = {"Nazaret", "Duque", 35}
my_list = list(my_set)
print(my_list) # ['Nazaret', 'Duque', 35]
print(my_list[0]) # Nazaret
```

> 🔹 Puedes convertir un set en lista con `list()`.  
> 🔹 Esto permite acceder a sus elementos por índice.

### Otras operaciones entre conjuntos

```python
my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
# {35, 'Python', 'Swift', 'C#', 'Nazaret', 'Duque', 'JavaScript', 'Kotlin'}

print(my_set) # {'Nazaret', 'Duque', 35}
print(my_new_set) # {35, 'Python', 'Swift', 'Nazaret', 'Duque', 'Kotlin'}
print(my_new_set.difference(my_set)) # {'Python', 'Swift', 'Kotlin'} Devuelve los elementos de my_new_set que no están en my_set
```

> 🔹 `union()` combina dos conjuntos, eliminando duplicados.  
> 🔹 `difference()` devuelve los elementos de un conjunto que no están en otro.  
> 🔹 También existen `intersection()` y `symmetric_difference()` para operaciones de teoría de conjuntos.

#### Resumen

- Los sets **no mantienen orden** y **no permiten duplicados**.
- Son **mutables**, pero solo aceptan elementos **inmutables** (por ejemplo, no se pueden incluir listas).
- Útiles para eliminar duplicados o realizar operaciones matemáticas entre colecciones.
- Se pueden transformar fácilmente en listas o usar en comprobaciones rápidas de pertenencia.

---

### Diccionarios [🔝 Volver al inicio](#)

Los **diccionarios** (`dict`) son estructuras de datos **no ordenadas** que almacenan información en **pares clave–valor**.  
Son **mutables**, no admiten claves duplicadas y permiten un acceso muy rápido a los datos.

#### Definición

```python
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

print(my_other_dict) # {'Nombre': 'Nazaret', 'Apellido': 'Duque', 'Edad': 35, 1: 'Python'}
print(my_dict) # {'Nombre': 'Nazaret', 'Apellido': 'Duque', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77}

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5
```

> 🔹 Las claves pueden ser de distintos tipos, pero deben ser **inmutables** (cadenas, números, tuplas…).  
> 🔹 Los valores pueden ser de cualquier tipo, incluso otros diccionarios o conjuntos.

#### Búsqueda

```python
print(my_dict[1]) # 1.77
print(my_dict["Nombre"]) # Nazaret

print("Duque" in my_dict) # False, busca por clave
print("Apellido" in my_dict) # True
```

> 🔹 El acceso se hace por **clave**, no por posición.  
> 🔹 El operador `in` verifica si existe una clave, no un valor.

#### Inserción

```python
my_dict["Calle"] = "Calle DuqueDev"
print(my_dict)
# {'Nombre': 'Nazaret', 'Apellido': 'Duque', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77, 'Calle': 'Calle DuqueDev'}
```

> 🔹 Si la clave no existe, se crea un nuevo par clave–valor.

#### Actualización

```python
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"]) # Pedro
```

> 🔹 Si la clave ya existe, se **sobrescribe su valor**.

#### Eliminación

```python
del my_dict["Calle"]
print(my_dict)
# {'Nombre': 'Pedro', 'Apellido': 'Duque', 'Edad': 35, 'Lenguajes': {'Swift', 'Python', 'Kotlin'}, 1: 1.77}
```

> 🔹 Con `del` se elimina una clave y su valor asociado.  
> 🔹 También existen métodos como `pop()` o `clear()` para eliminar o vaciar el diccionario.

#### Otras operaciones útiles

```python
print(my_dict.items())
# dict_items([('Nombre', 'Pedro'), ('Apellido', 'Duque'), ('Edad', 35), ('Lenguajes', {'Swift', 'Python', 'Kotlin'}), (1, 1.77)])
print(my_dict.keys())
# dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print(my_dict.values())
# dict_values(['Pedro', 'Duque', 35, {'Swift', 'Python', 'Kotlin'}, 1.77])
```

> 🔹 `items()` devuelve pares clave–valor.  
> 🔹 `keys()` devuelve todas las claves.  
> 🔹 `values()` devuelve los valores.

#### Crear diccionarios con `fromkeys()`

```python
my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}

my_new_dict = dict.fromkeys(my_dict, "DuqueDev")
print(my_new_dict)
# {'Nombre': 'DuqueDev', 'Apellido': 'DuqueDev', 'Edad': 'DuqueDev', 'Lenguajes': 'DuqueDev', 1: 'DuqueDev'}
```

> 🔹 `dict.fromkeys(iterable)` crea un nuevo diccionario con las claves del iterable y valores por defecto (`None` o el valor que se indique).

#### Trabajar con `values()`

```python
my_values = my_new_dict.values()
print(type(my_values)) # <class 'dict_values'>

print(my_new_dict.values())
# dict_values(['DuqueDev', 'DuqueDev', 'DuqueDev', 'DuqueDev', 'DuqueDev'])
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
# ['DuqueDev']

print(tuple(my_new_dict))
# ('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)

print(set(my_new_dict))
# {'Apellido', 1, 'Nombre', 'Edad', 'Lenguajes'}
```

> 🔹 `values()` devuelve un objeto de tipo `dict_values`, iterable pero no una lista.  
> 🔹 Se puede convertir a lista, tupla o conjunto.  
> 🔹 Convertir un diccionario con `tuple()` o `set()` devuelve solo las **claves**.

#### Resumen

- Los **diccionarios** almacenan pares clave–valor y permiten acceso rápido por clave.
- Las **claves deben ser únicas e inmutables**.
- Se pueden modificar, añadir o eliminar pares libremente.
- Métodos útiles: `keys()`, `values()`, `items()`, `get()`, `fromkeys()`.
- Son la estructura base para representar objetos o datos complejos en Python (por ejemplo, JSON).

---

## Condicionales y bucles [🔝 Volver al inicio](#)

Los **condicionales** y **bucles** son estructuras de control que permiten modificar el flujo de ejecución de un programa en función de condiciones o repeticiones.

---

### Condicionales (`if`, `elif`, `else`)

Los condicionales permiten ejecutar un bloque de código solo si se cumple una condición.

```python
my_condition = True

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")  # Si no se tabula esta línea, da error en tiempo de ejecución

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")
```

> 🔹 `if` evalúa una condición booleana.  
> 🔹 `elif` (else if) permite comprobar condiciones adicionales.  
> 🔹 `else` se ejecuta cuando ninguna condición previa se cumple.  
> 🔹 La indentación (tabulación) es **obligatoria** y define los bloques de código.

### Evaluación de valores

```python
my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")
```

> 🔹 En Python, los valores vacíos (`""`, `[]`, `{}`, `None`, `0`) se consideran **False** en una evaluación booleana.  
> 🔹 El operador `not` invierte el valor lógico.

### Operador ternario

Sintaxis: `a` if condition else `b`
Ejemplo:

```python
print("Es positivo" if 5 > 0 else "Es negativo")
```

> 🔹 Es una forma compacta de escribir condicionales simples en una línea.

---

### Bucles (`for` y `while`)

Los **bucles** permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o para recorrer secuencias.

#### Bucle `while`

```python
my_condition = 0

while my_condition < 5:
    print(my_condition)
    my_condition += 1
else:
    print("El while ha terminado")
```

> 🔹 `while` repite el bloque mientras la condición sea `True`.  
> 🔹 Se puede usar `else` tras un bucle: se ejecuta al finalizar sin interrupciones (`break`).

#### Bucle `for`

```python
my_list = [35, 24, 62, 52, 30, 17]

for element in my_list:
    print(element)

for i in range(5):
    print(i)
```

> 🔹 `for` recorre los elementos de una secuencia (lista, cadena, rango, etc.).  
> 🔹 `range(n)` genera una secuencia de 0 a n-1.

#### Control de flujo en bucles

```python
for i in range(10):
    if i == 3:
        continue  # Salta a la siguiente iteración
    elif i == 6:
        break  # Termina el bucle
    print(i)
else:
    print("Bucle finalizado sin interrupciones")
```

> 🔹 `continue` omite la iteración actual.  
> 🔹 `break` interrumpe completamente el bucle.  
> 🔹 El bloque `else` en un bucle solo se ejecuta si el bucle termina de forma natural (sin `break`).

### Resumen

- `if`, `elif`, `else` controlan decisiones.
- Los valores vacíos o `None` son falsos por defecto.
- `for` recorre secuencias; `while` repite hasta que la condición deja de cumplirse.
- `break`, `continue` y `else` modifican el comportamiento de los bucles.
- La indentación define los bloques de código: **es obligatoria en Python**.

> Consultar el script [09_loops](../basic/09_loops.py) para ver más ejemplos de bucles `for` y cómo recorrer iterables. También veremos más ejemplos cuando veamos `list comprehension` en python.

---

## Funciones [🔝 Volver al inicio](#)

Las **funciones** permiten agrupar instrucciones bajo un nombre para reutilizarlas, hacer el código más limpio y evitar repeticiones.  
Se definen con la palabra clave `def` y pueden recibir parámetros y devolver valores.

---

### Definición básica

```python
def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Esto es una función
# Esto es una función
# Esto es una función
```

> 🔹 Las funciones se definen con `def nombre_funcion():`.  
> 🔹 Se ejecutan llamándolas por su nombre.

### Función con parámetros de entrada (argumentos)

```python

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)              # 12
sum_two_values(54754, 71231)      # 125985
sum_two_values("5", "7")          # 57
sum_two_values(1.4, 5.2)          # 6.6
```

> 🔹 Los parámetros se indican entre paréntesis.  
> 🔹 Las anotaciones de tipo (`: int`) no son obligatorias, solo informativas.  
> 🔹 Python permite operar con diferentes tipos, pero el comportamiento depende del tipo de dato.

### Función con retorno

```python
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# 6.6
# 15
```

> 🔹 `return` devuelve un valor que puede guardarse o usarse más adelante.  
> 🔹 Si no se usa `return`, la función devuelve `None` por defecto.

### Parámetros por nombre (keyword arguments)

```python
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Duque", name="Nazaret")

# Nazaret Duque
```

> 🔹 Puedes pasar los argumentos en cualquier orden si indicas sus nombres al llamar a la función.  
> 🔹 Es útil para mejorar la legibilidad y evitar confusiones con el orden de los parámetros.

### Parámetros con valor por defecto

```python
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Nazaret", "Duque")
print_name_with_default("Nazaret", "Duque", "DuqueDev")

# Nazaret Duque Sin alias
# Nazaret Duque DuqueDev
```

> 🔹 Los valores por defecto se usan cuando no se pasa un argumento.  
> 🔹 Deben colocarse al final de la lista de parámetros.

### Parámetros arbitrarios (`*args`)

**Argumentos Variables:**

- El asterisco (`*`) permite que la función acepte un número variable de argumentos.
- Esto significa que puedes llamar a la función con cero, uno o más argumentos, y todos ellos se agruparán en una tupla.

**Cómo funciona:**
Los argumentos proporcionados después del asterisco (\*) se empaquetan en una tupla con el nombre
que aparece después del asterisco (texts en este caso). Dentro de la función, puedes trabajar con
esa tupla como lo harías con cualquier otra tupla en Python.

```python
def print_upper_texts(*texts):
    print(type(texts)) # <class 'tuple'>
    for text in texts: # Itera sobre cada elemento de la tupla 'texts'
        print(text.upper())  # Convierte cada texto en mayúsculas y lo imprime

print_upper_texts("Hola", "Python", "DuqueDev")
print_upper_texts("Hola")

'''
<class 'tuple'>
HOLA
PYTHON
DUQUEDEV
<class 'tuple'>
HOLA
'''
```

> 🔹 Los parámetros con `*` agrupan argumentos variables en una **tupla**.  
> 🔹 Se pueden iterar y manipular como cualquier colección.  
> 🔹 También existe `**kwargs` para argumentos **nombrados** variables (diccionario).

---

### Resumen

- Las funciones se definen con `def` y se ejecutan llamándolas.
- Pueden recibir **argumentos**, tener **valores por defecto**, y **devolver resultados** con `return`.
- Se pueden usar **anotaciones de tipo** para mejorar la legibilidad.
- `*args` y `**kwargs` permiten recibir argumentos variables.
- El uso de funciones mejora la **modularidad** y **reutilización** del código.

---

## Clases y excepciones [🔝 Volver al inicio](#)

---

### Clases y Programación Orientada a Objetos [🔝 Volver al inicio](#)

En Python, las **clases** permiten crear estructuras personalizadas que combinan **datos (atributos)** y **funciones (métodos)**.  
A diferencia de otros lenguajes como Java o C#, el modelo de objetos de Python es **altamente dinámico**:  
las clases son objetos en sí mismas, pueden modificarse en tiempo de ejecución y no existe una privacidad estricta.

> [Documentación oficial](https://docs.python.org/es/3/tutorial/classes.html)

#### Definición básica de una clase

Por convención, los nombres de las clases se escriben en PascalCase:

```python
class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

# <class '__main__.MyEmptyPerson'>
# <__main__.MyEmptyPerson object at 0x...>
```

> 🔹 En Python, **todo es un objeto**, incluso las clases.  
> 🔹 Cuando se define una clase, el intérprete ejecuta su código y crea un objeto de tipo `type`.  
> 🔹 `pass` se usa como marcador para definir estructuras vacías temporalmente.

#### Clase con constructor, métodos y encapsulamiento

En Python, los atributos se definen directamente en el constructor o incluso fuera de él.
A diferencia de otros lenguajes, no necesitas declararlos previamente.

**Encapsulamiento:**

- Los atributos públicos se definen normalmente.
- Los protegidos se prefijan con `_` (convención, no es estrictamente privado).
- Los privados se prefijan con `__` (esto aplica 'name mangling' para evitar colisiones de nombres).

```python
class Person:
    def __init__(self, name, surname, alias="Sin alias"):  # Constructor
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    # Los métodos se definen como funciones dentro de la clase y reciben self como primer parámetro.
    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person = Person("Nazaret", "Duque")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Nazaret", "Duque", "DuqueDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

'''
OUTPUT:
Nazaret Duque (Sin alias)
Nazaret
Nazaret Duque (Sin alias) está caminando
Nazaret Duque (DuqueDev)
Nazaret Duque (DuqueDev) está caminando
Héctor de León (El loco de los perros)
666
'''
```

> 🔹 Python **no aplica encapsulamiento real**: los atributos “privados” pueden accederse mediante `_Clase__atributo`.  
> 🔹 No existe una palabra clave `private` o `protected`; se usa **convención**, no restricción.  
> 🔹 `self` no es palabra reservada: solo es el nombre habitual del primer parámetro de los métodos.  
> 🔹 Los objetos son **dinámicos**: puedes modificar atributos o tipos de forma libre.

#### Métodos estáticos

```python
class Utilidad:
    @staticmethod  # opcional
    def sumar(a, b):
        return a + b

resultado = Utilidad.sumar(5, 10)
print(resultado)  # 15
```

> 🔹 Los métodos estáticos (`@staticmethod`) **no reciben** ni la instancia (`self`) ni la clase (`cls`).  
> 🔹 Se usan para funciones relacionadas con la clase, pero que no dependen de su estado interno.  
> 🔹 En Python, el decorador `@staticmethod` **no es obligatorio**, es solo una forma de aclarar la intención.

#### Atributos de clase (“estáticos”)

```python
class Configuracion:
    version = "1.0.0"

print(Configuracion.version)  # 1.0.0
Configuracion.version = "1.1.0"
print(Configuracion.version)  # 1.1.0

# Acceso desde una instancia:
config1 = Configuracion()
config2 = Configuracion()
print(config1.version)  # 1.1.0
print(config2.version)  # 1.1.0
```

> En Python, los llamados “atributos estáticos” son en realidad **atributos de clase**:
>
> - Se almacenan en el propio objeto `class`, no en las instancias.
> - Se comparten entre todas las instancias **mientras no se sobrescriban**.
> - Si una instancia asigna un valor al mismo nombre, crea su **propio atributo local**, ocultando el de clase.  
>   Esto los diferencia de los _static fields_ reales de Java o C#.

#### Métodos de clase

```python
class Configuracion:
    version = "1.0.0"

    @classmethod
    def obtener_version(cls):
        return cls.version

print(Configuracion.obtener_version())  # 1.0.0
```

> 🔹 `@classmethod` recibe la **clase** como primer parámetro (`cls`).  
> 🔹 Se usa para acceder o modificar atributos compartidos a nivel de clase.

#### Ejemplo completo con atributos y métodos estáticos y de clase

```python
class Banco:
    tasa_interes = 0.05  # Atributo de clase (compartido)

    def __init__(self, saldo):
        self.saldo = saldo  # Atributo de instancia (propio)

    def calcular_interes(self):
        return self.saldo * Banco.tasa_interes

    @staticmethod
    def info_bancaria():
        return "Este es el Banco ABC."

    @classmethod
    def actualizar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

print(Banco.info_bancaria())  # Este es el Banco ABC.

cliente = Banco(1000)
print(cliente.calcular_interes())  # 50.0

Banco.actualizar_tasa_interes(0.06)
print(cliente.calcular_interes())  # 60.0
```

> 🔹 `@staticmethod` define funciones auxiliares.  
> 🔹 `@classmethod` permite manipular los atributos de clase.  
> 🔹 En Python, el límite entre ambos es conceptual, no técnico: ambos son funciones asociadas al objeto `class`.

#### Polimorfismo

```python
class Vehiculo:
    def avanzar(self):
        return "El vehículo avanza"

class Bicicleta(Vehiculo):
    def avanzar(self):
        return "La bicicleta avanza pedaleando"

vehiculos = [Vehiculo(), Bicicleta()]

for v in vehiculos:
    print(v.avanzar())

# El vehículo avanza
# La bicicleta avanza pedaleando
```

> 🔹 Python aplica **polimorfismo dinámico**: las subclases pueden sobrescribir libremente métodos del padre.  
> 🔹 No existe sobrecarga de métodos por tipo o número de parámetros (solo la última definición cuenta).

#### Atributos dinámicos

```python
p = Person("Pedro", "Hdez")
p.edad = 36
print(p.edad)  # 36
```

> 🔹 Los objetos son **dinámicos**: puedes añadir atributos a una instancia en cualquier momento.  
> 🔹 Esto aporta flexibilidad, pero también puede generar errores difíciles de rastrear si se abusa.

#### Herencia

```python
class AnotherPerson(Person):
    def caminar(self):
        # Puedes usar super() para acceder a los métodos de la clase base
        return super().walk()

persona = AnotherPerson("Nazaret", "Duque")
print(persona.caminar())

# Nazaret Duque (Sin alias) está caminando
```

> 🔹 `super()` permite llamar a métodos de la clase base.  
> 🔹 Python admite herencia simple y múltiple.  
> 🔹 A diferencia de Java o C#, **no existe palabra clave “extends”**: la herencia se indica entre paréntesis.

#### Herencia múltiple y MRO (orden de resolución de métodos)

```python
class ClaseBase1:
    def metodo_base1(self):
        return "Método de ClaseBase1"

class ClaseBase2:
    def metodo_base2(self):
        return "Método de ClaseBase2"

class ClaseDerivada(ClaseBase1, ClaseBase2):
    pass

obj = ClaseDerivada()
print(obj.metodo_base1())  # Método de ClaseBase1
print(obj.metodo_base2())  # Método de ClaseBase2
```

**Orden de resolución de métodos (MRO):**

```python
class A:
    def saludar(self):
        return "Hola desde A"

class B(A):
    def saludar(self):
        return "Hola desde B"

class C(A):
    def saludar(self):
        return "Hola desde C"

class D(B, C):
    pass

d = D()
print(d.saludar())  # Hola desde B
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

> 🔹 En herencia múltiple, Python sigue el algoritmo **C3 Linearization**.  
> 🔹 Este orden puede consultarse con `__mro__` o `help(Clase)`.  
> 🔹 El orden de búsqueda de métodos es **dinámico** y depende de la jerarquía.
> 🔹 super() no significa "mi padre" sino "ve al siguiente en el MRO después de mí"

#### Ejemplo práctico de `super()` con herencia múltiple

```python
class A:
    def accion(self):
        print("Acción en A")

class B(A):
    def accion(self):
        super().accion()
        print("Acción en B")

class C(A):
    def accion(self):
        super().accion()
        print("Acción en C")

class D(B, C):
    def accion(self):
        super().accion()
        print("Acción en D")

d = D()
d.accion()

# Salida:
# Acción en A
# Acción en C
# Acción en B
# Acción en D
```

> 🔹 `super()` respeta el orden del MRO.  
> 🔹 Este comportamiento hace que la herencia múltiple en Python sea predecible y cooperativa.

#### Resumen

- En Python **todo es un objeto**, incluidas las clases.
- No hay encapsulamiento real, sino **convenciones** (`_protegido`, `__privado`).
- Los “atributos estáticos” son **atributos de clase** compartidos, no inmutables.
- `@staticmethod`, `@classmethod` y `super()` ofrecen gran flexibilidad en diseño de clases.
- No hay sobrecarga de métodos ni privacidad estricta.
- Python admite **herencia múltiple** con un sistema MRO claro y dinámico.
- Los objetos pueden modificarse **en tiempo de ejecución**, lo que lo hace muy poderoso (y también más propenso a errores si no se controla).

---

### Manejo de Excepciones [🔝 Volver al inicio](#)

El manejo de excepciones en Python permite **controlar errores en tiempo de ejecución** sin que el programa se interrumpa abruptamente.  
A diferencia de otros lenguajes como Java o C#, Python no requiere declarar las excepciones (no hay _checked exceptions_).  
Cualquier bloque de código puede lanzar una excepción, y el flujo de ejecución se maneja mediante `try`, `except`, `else` y `finally`.

#### Excepción base: `try` / `except`

```python
numberOne = 5
numberTwo = 1
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Se ha producido un error
```

> 🔹 Si ocurre un error dentro del bloque `try`, el control pasa inmediatamente al bloque `except`.  
> 🔹 Si no ocurre ningún error, el bloque `except` se omite.  
> 🔹 No es buena práctica usar `except:` sin especificar el tipo de excepción, ya que puede ocultar errores inesperados.

#### Flujo completo: `try` / `except` / `else` / `finally`

```python
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Se ha producido un error
# La ejecución continúa
```

> 🔹 `else` se ejecuta solo si no hubo errores.  
> 🔹 `finally` se ejecuta **siempre**, haya error o no (ideal para liberar recursos, cerrar archivos o conexiones).

#### Excepciones por tipo

```python
try:
    print(numberOne + int(numberTwo))
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Se ha producido un ValueError
```

> 🔹 Puedes capturar excepciones específicas, igual que en Java o C#.  
> 🔹 El orden importa: las excepciones más específicas deben ir primero.  
> 🔹 `ValueError` se lanza al intentar convertir tipos incompatibles (por ejemplo, `int("hola")`).  
> 🔹 `TypeError` ocurre cuando se usa un tipo de dato inapropiado para una operación.

#### Captura del objeto de excepción

```python
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)

# unsupported operand type(s) for +: 'int' and 'str'
```

> 🔹 `as` permite acceder al objeto de la excepción capturada.  
> 🔹 `Exception` es la **clase base** de casi todas las excepciones en Python (equivalente a `Throwable` en Java).  
> 🔹 Evita capturar `Exception` si puedes ser más específico.

#### Ejemplo con `ValueError`

```python
numberTwo = "hola"

try:
    print(numberOne + int(numberTwo))
    print("No se ha producido un error")
except ValueError as error:
    print(f"ValueError: {error}")
except Exception as my_random_error_name:
    print(f"Exception: {my_random_error_name}")

# ValueError: invalid literal for int() with base 10: 'hola'
```

> 🔹 Los mensajes de error pueden imprimirse o registrarse (logging).  
> 🔹 Python incluye jerarquías completas de excepciones integradas (`TypeError`, `KeyError`, `ZeroDivisionError`, etc.).  
> 🔹 Puedes definir tus propias excepciones creando una clase que herede de `Exception`.

#### Diferencias clave con otros lenguajes

- Python **no fuerza** el manejo de excepciones (no hay checked exceptions).
- Las excepciones son **objetos dinámicos**: no se declaran, se lanzan cuando ocurren.
- Puedes capturar múltiples tipos con una sola línea:

```python
except (ValueError, TypeError) as error:
    print(error)
```

> 🔹 No existe una sintaxis try-catch-finally como tal — except cumple el papel de catch.
> 🔹 Los bloques else y finally son opcionales pero muy útiles para controlar el flujo y limpiar recursos.

#### Excepciones personalizadas

Además de las excepciones integradas, puedes crear tus propias excepciones para representar errores específicos de tu aplicación.  
Esto mejora la legibilidad del código y permite un manejo más preciso de los fallos.

```python
# Definición de una excepción personalizada
class CustomError(Exception):
    """Excepción personalizada para errores específicos."""
    def __init__(self, mensaje, codigo=0):
        super().__init__(mensaje)
        self.codigo = codigo

# Lanzar la excepción
def dividir(a, b):
    if b == 0:
        raise CustomError("No se puede dividir entre cero", codigo=400)
    return a / b

# Manejo de la excepción
try:
    resultado = dividir(10, 0)
except CustomError as error:
    print(f"Error personalizado: {error} (código: {error.codigo})")

# Salida:
# Error personalizado: No se puede dividir entre cero (código: 400)
```

> 🔹 Para crear una excepción personalizada, basta con heredar de `Exception` (o de otra excepción específica).  
> 🔹 Puedes añadir atributos, mensajes y comportamiento propio.  
> 🔹 Se recomienda usar nombres que terminen en `Error` por convención (por ejemplo: `ValidationError`, `ConnectionError`, etc.).  
> 🔹 Se pueden lanzar con `raise`, igual que las excepciones integradas.

#### Resumen final

- Usa `try` / `except` para manejar errores sin interrumpir la ejecución.
- Especifica tipos concretos de excepción siempre que sea posible.
- Usa `else` para ejecutar código solo cuando no haya errores.
- Usa `finally` para limpiar recursos o cerrar conexiones.
- Puedes **crear tus propias excepciones** para hacer el código más expresivo y fácil de mantener.

> En Python, las excepciones no son solo para errores: también se utilizan para controlar el flujo del programa de manera elegante y explícita.

---

## Módulos [🔝 Volver al inicio](#)

Los **módulos** en Python son archivos `.py` que agrupan funciones, clases y variables para organizarlas y reutilizarlas fácilmente.  
Permiten dividir un programa grande en varios archivos más manejables.

### Ejemplo de módulo propio

Archivo: `my_module.py`

```python
Módulo para pruebas:
def sumValue(numberOne, numberTwo, numberThree):
    print(numberOne + numberTwo + numberThree)

def printValue(value):
    print(value)
```

> 🔹 Cada archivo `.py` puede considerarse un **módulo**.  
> 🔹 El nombre del archivo es el nombre del módulo (sin la extensión `.py`).  
> 🔹 Puedes importar ese módulo desde otro script ubicado en el mismo directorio.

### Importar módulos y funciones

```python
from math import pi as PI_VALUE  # Importar solo un elemento concreto (y renombrarlo)
import math                     # Importar todo el módulo
from my_module import sumValue, printValue  # Importar funciones específicas
import my_module                 # Importar todo el módulo propio

my_module.sumValue(5, 3, 1)  #Si importamos todo el módulo accedemos así
my_module.printValue("Hola Python!")

sumValue(5, 3, 1)  #Si importamos las funciones concretas podemos acceder solo con el nombre de la función
printValue("Hola python")

print(math.pi)  # 3.141592653589793
print(math.pow(2, 8)) # 256.0
print(PI_VALUE) # 3.141592653589793
```

### Tipos de importación

| Forma de importación         | Ejemplo                 | Cuándo usarla                                       |
| ---------------------------- | ----------------------- | --------------------------------------------------- |
| `import módulo`              | `import math`           | Para acceder a todas las funciones con `math.`      |
| `from módulo import función` | `from math import sqrt` | Cuando solo necesitas una parte específica          |
| `from módulo import *`       | `from math import *`    | No recomendable: puede causar conflictos de nombres |
| `import módulo as alias`     | `import math as m`      | Para abreviar nombres largos de módulo              |

> 🔹 La importación es **perezosa**: solo se ejecuta una vez por módulo.  
> 🔹 Si un módulo se importa de nuevo, Python usa una versión en caché desde `sys.modules`.

### Resumen

- Un **módulo** es cualquier archivo `.py` que contiene código reutilizable.
- Los módulos ayudan a **organizar** y **modularizar** el código.
- Se pueden importar de muchas formas: completas, selectivas o con alias.
- Python ejecuta el código del módulo solo una vez por sesión y lo guarda en caché.

> En resumen: los módulos son la base de la **reutilización de código en Python**.  
> Cualquier archivo `.py` puede ser un módulo.

---

## 🔗 Navegación [🔝 Volver al inicio](#)

⬅️ [Volver al índice principal](../README.md) | [Siguiente lección ➡️](./intermediate.md)
