# Python Intermedio

---

## Índice

1. [Fechas y tiempos](#fechas-y-tiempos--volver-al-inicio)
2. [List comprehensions y lambdas](#list-comprehensions--volver-al-inicio)
3. [Funciones de orden superior](#funciones-de-orden-superior--volver-al-inicio)
4. [Gestión de errores](#gestión-de-errores--volver-al-inicio)
5. [Manejo de archivos](#manejo-de-archivos--volver-al-inicio)
6. [Expresiones regulares](#expresiones-regulares--volver-al-inicio)
7. [Gestión de paquetes y módulos](#gestión-de-paquetes-y-módulos--volver-al-inicio)
8. [Arrays en python](#arrays-en-python--volver-al-inicio)
9. [Challenges: Retos de programación sencillos](#retos-de-programación-sencillos--volver-al-inicio)

---

## Fechas y tiempos [🔝 Volver al inicio](#)

El módulo `datetime` de la biblioteca estándar de Python permite **trabajar con fechas, horas, zonas horarias y diferencias de tiempo** (timedelta).  
Python separa estos conceptos en varios objetos: `datetime`, `date`, `time`, `timedelta` y `timezone`.

### Importación de clases del módulo `datetime`

```python
from datetime import timedelta, date, time, datetime, timezone
```

> 🔹 `datetime`: combina fecha y hora.  
> 🔹 `date`: solo fecha (año, mes, día).  
> 🔹 `time`: solo hora (hora, minuto, segundo).  
> 🔹 `timedelta`: representa diferencias entre fechas u horas.  
> 🔹 `timezone`: define zonas horarias (como UTC).

### Datetime — fecha y hora completas

```python
now = datetime.now()
print(now)

# Ejemplo de salida:
# 2025-10-16 18:42:11.123456

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

# Salida:
# 2025
# 10
# 16
# 18
# 42
# 11
# 1739706131.123456
```

> 🔹 `datetime.now()` devuelve un objeto con la fecha y hora actual del sistema.  
> 🔹 `timestamp()` devuelve una **representación numérica única** de la fecha (segundos desde 1970-01-01 UTC).  
> 🔹 Todos los campos (`year`, `month`, `day`, etc.) son accesibles como atributos.

### Crear fechas personalizadas

```python
year_2023 = datetime(2023, 1, 1)
print_date(year_2023)

# Salida:
# 2023
# 1
# 1
# 0
# 0
# 0
# 1672531200.0
```

> 🔹 Para crear un `datetime`, se necesitan al menos tres argumentos: `año`, `mes` y `día`.  
> 🔹 Los parámetros de hora son opcionales y, si se omiten, se asumen como 0.

### Objeto `time` — solo hora

```python
current_time = time(21, 6, 0)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Salida:
# 21
# 6
# 0
```

> 🔹 `time()` define una hora sin fecha asociada.  
> 🔹 Ideal para representar horarios (ej. hora de apertura o cierre).

### Objeto `date` — solo fecha

```python
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Ejemplo de salida:
# 2025
# 10
# 16

current_date = date(2022, 10, 6)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Salida:
# 2022
# 10
# 6

# Crear una nueva fecha modificando la existente
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)  # 11
```

> 🔹 `date.today()` devuelve la fecha actual del sistema.  
> 🔹 Los objetos `date` son **inmutables**, por lo que para “modificarlos” hay que crear uno nuevo.

### Operaciones con fechas

```python
diff = year_2023 - now
print(diff)

# Salida (ejemplo):
# -1023 days, 5:17:48.876544

diff = year_2023.date() - current_date
print(diff)

# Salida:
# 426 days, 0:00:00
```

> 🔹 Se pueden restar objetos `datetime` o `date` entre sí (deben ser del mismo tipo).  
> 🔹 El resultado es un objeto `timedelta`, que representa la diferencia entre ambos.

### Timedelta — diferencias de tiempo

```python
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

# Salida:
# 31 days, 0:00:00
# 791 days, 0:03:20.000200
```

> 🔹 Un `timedelta` puede representar días, segundos, microsegundos o semanas.  
> 🔹 Permite sumar o restar intervalos de tiempo.

### Zonas horarias

```python
print(datetime.now())
print(datetime.now(timezone.utc))

# Ejemplo de salida:
# 2025-10-16 18:42:11.123456
# 2025-10-16 17:42:11.123456+00:00
```

> 🔹 `datetime.now()` sin argumentos produce un objeto **naive**, sin información de zona horaria.  
> 🔹 `datetime.now(timezone.utc)` crea un objeto **aware**, que sí tiene información de zona horaria (en este caso, UTC).  
> 🔹 Es importante usar fechas “aware” al trabajar con servidores o aplicaciones distribuidas.

### Resumen

- `datetime`, `date`, `time` y `timedelta` permiten manipular fechas y horas de manera flexible.
- `datetime.now()` devuelve la fecha y hora actuales.
- Las operaciones entre fechas devuelven `timedelta`.
- Usa objetos “aware” (`timezone.utc`) cuando necesites precisión horaria global.
- Los objetos `date` y `time` son inmutables.

> En Python, el módulo `datetime` unifica todo lo necesario para gestionar el tiempo de forma precisa, sin depender de librerías externas.

---

## List Comprehensions y Lambdas [🔝 Volver al inicio](#)

En esta sección aprenderás dos de las construcciones más potentes y características de Python:  
las **List Comprehensions**, que permiten crear listas en una sola línea de código,  
y las **funciones lambda**, que permiten definir funciones anónimas breves.

---

### List Comprehensions [🔝 Volver al inicio](#)

Las _list comprehensions_ son una forma concisa de **crear listas derivadas de iterables** (como `range()`, listas, sets, etc.) en una sola línea de código.

---

#### Ejemplo básico

```python
my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)
# [0, 1, 2, 3, 4, 5, 6, 7]

my_range = range(8)
print(list(my_range))
# [0, 1, 2, 3, 4, 5, 6, 7]
```

> 🔹 `range(n)` genera una secuencia de enteros desde `0` hasta `n - 1`.  
> 🔹 `list(range(n))` convierte ese rango en una lista.

#### Creación rápida de listas

```python
my_list = [i + 1 for i in range(8)]
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8]
```

> 🔹 Esta sintaxis equivale a usar un bucle `for` para rellenar una lista.  
> 🔹 Dentro de los corchetes, la primera parte indica **qué hacer con cada elemento**, y después de `for` **de dónde vienen los datos**.

#### Comparación con un bucle clásico

```python
my_other_list = []
for i in range(8):
    my_other_list.append(i + 1)
print(my_other_list)
# [1, 2, 3, 4, 5, 6, 7, 8]
```

> 🔹 La _list comprehension_ es más compacta y legible, pero hace lo mismo.

#### Ejemplos con operaciones

```python
my_list = [i * 2 for i in range(8)]
print(my_list)
# [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)]
print(my_list)
# [0, 1, 4, 9, 16, 25, 36, 49]
```

> 🔹 Puedes realizar cualquier operación dentro de la expresión inicial (`i * 2`, `i * i`, etc.).  
> 🔹 También puedes llamar a funciones o usar condicionales dentro de una _list comprehension_.

#### Usando funciones personalizadas

```python
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)
# [5, 6, 7, 8, 9, 10, 11, 12]
```

> 🔹 Puedes invocar funciones dentro de la expresión.  
> 🔹 Esto hace que las _list comprehensions_ sean muy potentes para procesar datos de forma funcional y declarativa.

#### Consejo

Las _list comprehensions_ son ideales para listas **pequeñas o medianas**.  
Si procesas colecciones muy grandes, usa [generadores](https://ellibrodepython.com/yield-python) o **funciones con `yield`** para evitar cargar toda la lista en memoria.

---

### Lambdas [🔝 Volver al inicio](#)

Una **lambda** en Python se define con la sintaxis `lambda argumentos: expresión` y debe caber en **una única expresión** (sin `return`, sin varias sentencias).

```python
# Definición normal de función
def sum_two_values(
    first_value, second_value): return first_value + second_value

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4)) # 11
```

> Aquí se está creando una **lambda** dentro de una función (closure): la lambda captura `value`.

#### Uso típico con funciones de orden superior (mini-ejemplos)

```python
nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))
# [2, 4, 6]

print(list(filter(lambda x: x % 2 == 0, nums)))
# [2]

print(sorted(["aa", "b", "ccc"], key=lambda s: len(s)))
# ['b', 'aa', 'ccc']
```

### Notas rápidas

- Lambdas: solo **expresiones**; para lógica no trivial, usa `def` por legibilidad.
- Son ideales como **argumentos** de `map`, `filter`, `sorted`, `sorted(key=...)`, etc.
- Una lambda es una función como cualquier otra (objeto de primera clase), solo que **anónima** y de **una línea**.

---

## Funciones de orden superior [🔝 Volver al inicio](#)

En Python, las **funciones son ciudadanos de primera clase** (_first-class citizens_):  
pueden pasarse como argumentos, devolverse como resultados y almacenarse en variables.  
Las **funciones de orden superior** son aquellas que **reciben o devuelven otras funciones**.

---

### Ejemplo básico de funciones de orden superior

```python
from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))   # 8
print(sum_two_values_and_add_value(5, 2, sum_five))  # 12
```

> 🔹 `sum_two_values_and_add_value` recibe como argumento otra función (`f_sum`).  
> 🔹 Esto permite modificar el comportamiento dinámicamente según la función que se le pase.  
> 🔹 Este patrón es común en programación funcional, callbacks y estrategias personalizadas.

### Closures (funciones anidadas que recuerdan su contexto)

Un **closure** es una función interna que **recuerda los valores del entorno** donde fue creada, incluso después de que la función exterior haya terminado de ejecutarse.

```python
def sum_ten(original_value):
    def add(value):
        return value * (10 + original_value)
    return add

add_closure = sum_ten(1)
print(add_closure(5))        # 55
print((sum_ten(5))(1))       # 15
print((sum_ten(1))(5))       # 55
```

> 🔹 `sum_ten` devuelve una función (`add`) que recuerda el valor de `original_value`.  
> 🔹 Los closures son la base de los decoradores y muchos patrones funcionales en Python.  
> 🔹 Aquí, cada llamada a `sum_ten(x)` devuelve una función personalizada que “recuerda” el valor `x`.

### Funciones de orden superior integradas

Python incluye varias funciones de orden superior muy comunes: `map()`, `filter()` y `reduce()`.

#### `map()`

Aplica una función a cada elemento de un iterable y devuelve un objeto `map`.

```python
numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
# [4, 10, 20, 42, 6, 60]

print(list(map(lambda number: number * 2, numbers)))
# [4, 10, 20, 42, 6, 60]
```

> 🔹 `map(func, iterable)` → aplica `func` a cada elemento.  
> 🔹 Devuelve un iterador, por lo que se suele convertir en lista.  
> 🔹 Es ideal para transformaciones rápidas sin usar bucles explícitos.

#### `filter()`

Devuelve los elementos del iterable que cumplen una condición.  
La función pasada debe devolver un **booleano** (`True`/`False`).

```python
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
# [21, 30]

print(list(filter(lambda number: number > 10, numbers)))
# [21, 30]
```

> 🔹 `filter(func, iterable)` filtra elementos según un criterio.  
> 🔹 La función debe devolver `True` para incluir el elemento.  
> 🔹 Es más expresivo y claro que usar bucles con condiciones.

#### `reduce()`

`reduce()` aplica una función acumulativa a los elementos de un iterable, reduciéndolos a un solo valor.  
No viene cargada por defecto, sino que hay que importarla desde `functools`.

```python
def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))
# 71
```

> 🔹 `reduce(func, iterable)` aplica `func` entre los elementos de izquierda a derecha.  
> 🔹 Equivale a combinar los valores paso a paso:  
>  (((2 + 5) + 10) + 21) + 3 + 30 → 71  
> 🔹 Se usa frecuentemente para sumar, combinar o acumular resultados.

### En resumen

| Función    | Qué hace                               | Devuelve              | Ejemplo            |
| ---------- | -------------------------------------- | --------------------- | ------------------ |
| `map()`    | Aplica una función a cada elemento     | Iterador transformado | Doblar cada número |
| `filter()` | Filtra los elementos según un criterio | Iterador filtrado     | Números > 10       |
| `reduce()` | Acumula todos los valores en uno solo  | Valor único           | Suma total         |

> En Python, las funciones de orden superior, los closures y las lambdas forman la base del estilo **funcional**,  
> que permite escribir código más expresivo, limpio y reutilizable.

---

## Gestión de errores [🔝 Volver al inicio](#)

Python dispone de un sistema robusto de **excepciones integradas** que detecta y gestiona los errores durante la ejecución del programa.  
Cada tipo de error se representa mediante una clase específica derivada de `Exception`.  
Conocer estos errores comunes te ayudará a **depurar** y **prevenir fallos** en tu código.

### Errores más comunes en Python

A continuación se muestran ejemplos de los errores más habituales con su causa y solución.

#### SyntaxError — Error de sintaxis

```python
print "¡Hola comunidad!"  # Falta paréntesis → provoca SyntaxError
```

```python
print("¡Hola comunidad!")
```

> 🔹 Ocurre cuando el código no respeta las reglas de la sintaxis de Python.  
> 🔹 El error se detecta antes de ejecutar el programa.  
> 🔹 Ejemplo: falta de paréntesis, comillas, dos puntos o indentación incorrecta.

#### NameError — Variable no definida

```python
# language = "Spanish"
print(language) # NameError: name 'language' is not defined
```

> 🔹 Se lanza cuando intentas usar una variable o función que no existe en el ámbito actual.  
> 🔹 Asegúrate de definir las variables antes de usarlas.

#### IndexError — Índice fuera de rango

```python
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])      # Python
print(my_list[4])      # JavaScript
print(my_list[-1])     # JavaScript
print(my_list[5])    # IndexError: list index out of range
```

> 🔹 Ocurre al acceder a una posición inexistente de una lista (índice demasiado alto o negativo).  
> 🔹 Usa `len(lista)` para comprobar el tamaño antes de acceder a un índice.

#### ModuleNotFoundError — Módulo inexistente

```python
import maths  # ModuleNotFoundError: No module named 'maths'
```

> 🔹 Se lanza cuando intentas importar un módulo que no existe o el nombre está mal escrito.  
> 🔹 Verifica el nombre del módulo o su instalación (`pip install nombre_modulo`).

#### AttributeError — Atributo inexistente

```python
print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'
```

> 🔹 Ocurre cuando accedes a un atributo o método que no existe dentro de un objeto o módulo.  
> 🔹 Python distingue entre mayúsculas y minúsculas, por lo que `math.PI` y `math.pi` no son lo mismo.

#### KeyError — Clave no encontrada en diccionario

```python
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])     # 35
print(my_dict["Apelido"])  # KeyError: 'Apelido'
print(my_dict["Apellido"]) # Moure
```

> 🔹 Ocurre al intentar acceder a una clave inexistente.  
> 🔹 Usa el método `.get()` para evitar el error y devolver un valor por defecto:
> `my_dict.get("Apelido", "No existe")`.

#### TypeError — Operación con tipos incompatibles

```python
print(my_list["0"])  # TypeError: list indices must be integers or slices, not str
print(my_list[0])       # Python
print(my_list[False])   # Python
```

> 🔹 Se lanza cuando se intenta realizar una operación entre tipos incompatibles.  
> 🔹 Ejemplo: sumar un número y una cadena, o usar un índice de tipo incorrecto.

#### ImportError — Error en la importación

```python
from math import PI  # ImportError: cannot import name 'PI' from 'math'
print(pi)  # 3.141592653589793
```

> 🔹 Sucede cuando intentas importar algo que no existe dentro del módulo.  
> 🔹 Verifica que el nombre del atributo o función sea correcto (`dir(math)` puede ayudarte).

#### ValueError — Conversión de tipo inválida

```python
my_int = int("10 Años")  # ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10")
print(type(my_int))  # <class 'int'>
```

> 🔹 Aparece cuando el tipo de dato es correcto pero su **valor no lo es** para la operación.  
> 🔹 Ejemplo: convertir texto no numérico a entero con `int()`.

#### ZeroDivisionError — División entre cero

```python
print(4 / 0)  # ZeroDivisionError: division by zero
print(4 / 2)    # 2.0
```

> 🔹 Ocurre al intentar dividir un número entre cero.  
> 🔹 Comprueba el divisor antes de realizar la operación o maneja la excepción con `try/except`.

### Resumen

| Tipo de error       | Cuándo ocurre         | Ejemplo típico                          |
| ------------------- | --------------------- | --------------------------------------- |
| `SyntaxError`       | Error de sintaxis     | Falta un paréntesis o sangría           |
| `NameError`         | Variable no definida  | Usar una variable no declarada          |
| `IndexError`        | Índice fuera de rango | Acceder a posición inexistente en lista |
| `KeyError`          | Clave no encontrada   | Buscar una clave errónea en diccionario |
| `TypeError`         | Tipos incompatibles   | Sumar cadena + número                   |
| `ValueError`        | Valor incorrecto      | Convertir “10 años” con `int()`         |
| `AttributeError`    | Atributo inexistente  | `math.PI` en lugar de `math.pi`         |
| `ImportError`       | Fallo en importación  | Importar nombre erróneo de módulo       |
| `ZeroDivisionError` | División entre cero   | `4 / 0`                                 |

> Python detecta y lanza automáticamente estos errores durante la ejecución.  
> Puedes prevenirlos con comprobaciones (`if`, `len`, `get`) o gestionarlos con **excepciones** (`try/except`).

## Manejo de archivos [🔝 Volver al inicio](#)

Python ofrece herramientas integradas para **crear, leer, modificar y eliminar archivos** de texto, CSV, JSON, XML y muchos otros formatos.  
El manejo de archivos es una de las tareas más comunes en automatización, análisis de datos y desarrollo de aplicaciones.

---

### Archivos de texto (.txt)

Python permite trabajar con archivos de texto mediante la función integrada `open()`.  
Esta función devuelve un objeto archivo y acepta varios **modos de apertura**:

| Modo   | Descripción                              |
| ------ | ---------------------------------------- |
| `"r"`  | Solo lectura (por defecto)               |
| `"w"`  | Escritura (crea o sobrescribe)           |
| `"a"`  | Añadir al final del archivo              |
| `"r+"` | Lectura y escritura                      |
| `"w+"` | Escritura y lectura (crea o sobrescribe) |

#### Ejemplo básico

```python
with open("Intermediate/my_file.txt", "w+") as txt_file:
    txt_file.write("Mi nombre es Nazaret\nMi apellido es Duque\n35 años\nY mi lenguaje preferido es Python")

# Reabrir para lectura
with open("Intermediate/my_file.txt", "r") as txt_file:
    for line in txt_file.readlines():
        print(line)

# Reabrir para agregar contenido al final
with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nAunque también me gusta Kotlin\nY Swift")

txt_file.close() # Cerramos recurso
```

> 🔹 `with` gestiona automáticamente el cierre del archivo (no hace falta `close()`).  
> 🔹 Los archivos se leen línea a línea con `readline()` o todas a la vez con `readlines()`.  
> 🔹 El modo `"a"` permite añadir texto sin sobrescribir el contenido existente.  
> 🔹 Es buena práctica cerrar siempre los archivos, incluso si no hay errores.

### Operaciones comunes con `os` (rutas y archivos)

Además de `open()`, la librería estándar `os` se usa mucho para trabajar con rutas y gestionar archivos.

```python
import os

base_dir = "intermediate"
file_name = "notas.txt"
file_path = os.path.join(base_dir, file_name)

# Crear carpeta si no existe
os.makedirs(base_dir, exist_ok=True)

# Crear/escribir archivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Primera línea\n")

# Verificar existencia
print(os.path.exists(file_path))  # True
print(os.path.isfile(file_path))  # True

# Listar contenido de una carpeta
print(os.listdir(base_dir))
```

```python
import os

old_path = os.path.join("intermediate", "notas.txt")
new_path = os.path.join("intermediate", "notas_v2.txt")

# Renombrar archivo
if os.path.exists(old_path):
    os.rename(old_path, new_path)

# Obtener tamaño en bytes
if os.path.exists(new_path):
    print(os.path.getsize(new_path))

# Eliminar archivo
if os.path.exists(new_path):
    os.remove(new_path)
```

> 🔹 `os.path.join()` crea rutas portables (Windows, Linux, macOS).  
> 🔹 `os.makedirs(..., exist_ok=True)` evita errores si la carpeta ya existe.  
> 🔹 Comprueba siempre con `exists()` antes de renombrar o eliminar.

### También con `pathlib` (alternativa moderna)

Para operaciones de rutas/archivos, `pathlib` suele ser más legible y expresivo.

```python
from pathlib import Path

base_dir = Path("intermediate")
file_path = base_dir / "notas_pathlib.txt"

base_dir.mkdir(parents=True, exist_ok=True)
file_path.write_text("Hola desde pathlib\n", encoding="utf-8")

print(file_path.exists())   # True
print(file_path.is_file())  # True
print([p.name for p in base_dir.iterdir()])

new_path = base_dir / "notas_pathlib_v2.txt"
file_path.rename(new_path)
print(new_path.stat().st_size)
new_path.unlink()
```

> 🔹 El operador `/` aquí no representa una división numérica; en pathlib, está sobrecargado para significar "unir partes de la ruta". Esto es preferible a la concatenación manual de cadenas porque es seguro para cualquier plataforma (por ejemplo, utiliza el separador correcto tanto en Windows como en Linux/macOS).
> 
> 🔹 Con `parents=True`, Python también creará cualquier carpeta de nivel superior (padre) que falte en la ruta, no solo el directorio final. Con `exist_ok=True`, no se producirá ningún error si el directorio ya existe, lo que hace que la operación sea segura para ejecutarse repetidamente. Sin estos parámetros, la falta de carpetas superiores o la existencia previa del directorio de destino podrían generar excepciones.
> 
> 🔹 `base_dir.iterdir()` devuelve cada ruta hija (archivos y subdirectorios) una por una.
> 
> 🔹 `print(new_path.stat().st_size)` lee los metadatos del sistema de archivos con `stat()` e imprime el tamaño del archivo en bytes a través de `st_size`. Esto confirma que el archivo renombrado sigue presente y muestra su tamaño actual.
> 
> 🔹 Finalmente, `new_path.unlink()` elimina ese archivo del disco. Un error común es que `unlink()` elimina archivos, no directorios, y genera un error si el archivo no existe, a menos que se utilice `missing_ok=True`.

### `os` vs `pathlib`: ¿cuándo usar cada uno?

- Usa `pathlib` en código nuevo cuando trabajes principalmente con rutas y archivos (más claro y orientado a objetos).
- Usa `os` cuando también necesites utilidades del sistema operativo: variables de entorno (`os.environ`), directorio actual (`os.getcwd()`), procesos (`os.system()`), etc.
- Ambos son estándar de Python y pueden convivir en el mismo proyecto.

### Archivos JSON (.json)

El formato JSON es ideal para **almacenar datos estructurados** (diccionarios, listas…).  
Python ofrece el módulo `json` para convertir entre objetos de Python y texto JSON.

```python
json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Nazaret",
    "surname": "Duque",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://Duque.dev"
}

json.dump(json_test, json_file, indent=2)
json_file.close()

# Leer JSON
with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# Salida:
# {'name': 'Nazaret', 'surname': 'Duque', 'age': 35, 'languages': ['Python', 'Swift', 'Kotlin'], 'website': 'https://Duque.dev'}
# <class 'dict'>
# Nazaret
```

> 🔹 `json.dump(objeto, archivo)` escribe un diccionario en un archivo JSON.  
> 🔹 `json.load(archivo)` convierte el contenido de un JSON a un diccionario.  
> 🔹 La indentación (`indent=2`) mejora la legibilidad del archivo.

### Archivos CSV (.csv)

El formato CSV (valores separados por comas) es común en hojas de cálculo y bases de datos.  
Python ofrece el módulo `csv` para escribir y leer archivos de este tipo.

```python
csv_file = open("Intermediate/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Nazaret", "Duque", 35, "Python", "https://Duque.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])
csv_file.close()

# Leer CSV
with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# Salida:
# name,surname,age,language,website
# Nazaret,Duque,35,Python,https://Duque.dev
# Roswell,,2,COBOL,
```

> 🔹 `csv.writer()` crea un escritor que genera líneas separadas por comas.  
> 🔹 Cada fila se añade con `.writerow(lista_de_valores)`.  
> 🔹 Al leer, se puede usar `.reader()` o `readlines()`.

---

### Archivos XML (.xml)

El formato XML se usa para **estructurar datos jerárquicos**.  
Python incluye el módulo `xml.etree.ElementTree` para crear y procesar XML fácilmente.

```python
import xml.etree.ElementTree as ET

root = ET.Element("data")
person = ET.SubElement(root, "person")
ET.SubElement(person, "name").text = "Nazaret"
ET.SubElement(person, "surname").text = "Duque"
ET.SubElement(person, "age").text = "35"
ET.SubElement(person, "language").text = "Python"

tree = ET.ElementTree(root)
with open("Intermediate/my_file.xml", "wb") as xml_file:
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
```

El archivo creado:

```xml
<?xml version="1.0" ?>
<data>
  <person>
    <name>Nazaret</name>
    <surname>Duque</surname>
    <age>35</age>
    <language>Python</language>
  </person>
</data>
```

Lectura del archivo:

```python
# Leer XML
tree = ET.parse("Intermediate/my_file.xml")
root = tree.getroot()

for person in root.findall("person"):
    name = person.find("name").text
    surname = person.find("surname").text
    age = person.find("age").text
    language = person.find("language").text
    print(f"Nombre: {name}, Apellido: {surname}, Edad: {age}, Lenguaje: {language}")

# Salida:
# Nombre: Nazaret, Apellido: Duque, Edad: 35, Lenguaje: Python
```

> 🔹 `ET.Element()` crea el elemento raíz.  
> 🔹 `ET.SubElement()` crea nodos hijos.  
> 🔹 `tree.write()` guarda el XML.  
> 🔹 `tree.getroot()` y `findall()` permiten recorrer la estructura.

---

#### Alternativa: XML con `minidom` (más legible)

Este enfoque genera un XML **formateado** y fácil de leer, con sangría y saltos de línea.

```python
import xml.dom.minidom as minidom
doc = minidom.Document()
root = doc.createElement("data")
doc.appendChild(root)

person = doc.createElement("person")
root.appendChild(person)

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

with open("Intermediate/my_file.xml", "w", encoding="utf-8") as xml_file:
    xml_file.write(doc.toprettyxml(indent="  "))

# Lectura
from xml.dom import minidom
doc = minidom.parse("Intermediate/my_file.xml")
persons = doc.getElementsByTagName("person")
for person in persons:
    name = person.getElementsByTagName("name")[0].firstChild.data
    surname = person.getElementsByTagName("surname")[0].firstChild.data
    age = person.getElementsByTagName("age")[0].firstChild.data
    language = person.getElementsByTagName("language")[0].firstChild.data
    print(f"Nombre: {name}, Apellido: {surname}, Edad: {age}, Lenguaje: {language}")
```

> 🔹 `minidom` genera XML con formato legible (“pretty print”).  
> 🔹 Ideal para visualizar estructuras complejas o crear documentos configurables.

### Resumen

| Formato | Módulo                             | Operaciones básicas                     |
| ------- | ---------------------------------- | --------------------------------------- |
| `.txt`  | Integrado (`open`)                 | Leer y escribir texto plano             |
| `.json` | `json`                             | Serializar diccionarios y listas        |
| `.csv`  | `csv`                              | Leer y escribir datos tabulares         |
| `.xml`  | `xml.etree.ElementTree`, `minidom` | Crear y parsear estructuras jerárquicas |

> Python proporciona soporte nativo para los formatos de datos más comunes,  
> con sintaxis simple, manejo seguro de recursos y total portabilidad.

---

## Expresiones regulares [🔝 Volver al inicio](#)

Las **expresiones regulares (regex)** permiten buscar, validar y transformar texto con patrones.  
En Python se usa el módulo `re` y funciones como `match`, `search`, `findall`, `split` y `sub`.

---

### Expresiones regulares

#### Coincidencia desde el inicio: `re.match`

```python
from datetime import datetime
import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)                         # <re.Match object; span=(0, 18), match='Esta es la lección'>
start, end = match.span()            # (0, 18)
print(my_string[start:end])          # Esta es la lección

match = re.match("Esta no es la lección", my_other_string)
if match is not None:
    print(match)                     # <re.Match object; span=(0, 22), match='Esta no es la lección'>
    start, end = match.span()
    print(my_other_string[start:end])# Esta no es la lección

print(re.match("Expresiones Regulares", my_string))  # None
```

> `match` exige que el patrón coincida **desde el inicio** de la cadena.  
> `re.I` (o `re.IGNORECASE`) hace la búsqueda **case-insensitive**.

#### Coincidencia en cualquier posición: `re.search`

```python
search = re.search("lección", my_string, re.I)
print(search)                        # <re.Match ...>
start, end = search.span()
print(my_string[start:end])          # lección
```

> `search` encuentra la **primera** coincidencia en cualquier parte del texto.

#### Todas las coincidencias: `re.findall`

```python
findall = re.findall("lección", my_string, re.I)
print(findall)                       # ['lección', 'Lección']
```

> `findall` devuelve una **lista** con todas las coincidencias.

#### Dividir texto: `re.split`

```python
print(re.split(":", my_string))
# ['Esta es la lección número 7', ' Lección llamada Expresiones Regulares']
```

> `split` divide por el patrón y devuelve una lista.

#### Sustitución: `re.sub`

```python
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
# Esta es la LECCIÓN número 7: LECCIÓN llamada Expresiones Regulares

print(re.sub("Expresiones Regulares", "RegEx", my_string))
# Esta es la lección número 7: Lección llamada RegEx
```

> `sub(patrón, reemplazo, texto)` reemplaza todas las apariciones del patrón.

### Patrones de expresiones regulares

```python
pattern = r"[lL]ección"
print(re.findall(pattern, my_string))
# ['lección', 'Lección']

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))
# ['lección', 'Lección', 'Expresiones']

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
# ['7']
print(re.search(pattern, my_string))
# <re.Match object; span=(27, 28), match='7'>

pattern = r"\d"
print(re.findall(pattern, my_string))
# ['7']

pattern = r"\D"
print(re.findall(pattern, my_string))
# [lista de todos los caracteres no numéricos; muy larga]

pattern = r"[l].*"
print(re.findall(pattern, my_string))
# ['la lección número 7: Lección llamada Expresiones Regulares']

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))      # <re.Match ...>
print(re.search(pattern, email))     # <re.Match ...>
print(re.findall(pattern, email))    # ['mouredev@mouredev.com']

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))    # ['mouredev@mouredev.com.mx']
```

> `\d` equivale a `[0-9]`; `\D` es lo contrario (no dígito).  
> `.*` es “cualquier secuencia” (codiciosa).  
> Los anchors `^` y `$` fijan el patrón al **inicio** y **final** de la cadena (útil para validaciones).
> Para aprender y validar expresiones regulares: [https://regex101.com](https://regex101.com)

### Compilar patrones con `re.compile` (eficiencia y legibilidad)

A veces es útil compilar una expresión regular para reutilizarla varias veces de forma eficiente.
El método `re.compile(patrón)` permite "precompilar" una expresión regular.
Esto crea un objeto de tipo re.Pattern que se puede reutilizar, lo cual mejora la legibilidad y eficiencia si vas a usar la expresión varias veces.

**Ejemplo:**

```python
# Queremos encontrar fechas tipo 'YYYY-MM-DD' entre comillas simples
regex_fecha = re.compile(r"'(\d{4}-\d{2}-\d{2})'")
print(type(regex_fecha))             # <class 're.Pattern'>
print(regex_fecha)                   # re.compile("'(\\d{4}-\\d{2}-\\d{2})'")
```

Una vez compilada, puedes usar métodos como:

- regex_fecha.match(cadena)
- regex_fecha.search(cadena)
- regex_fecha.findall(cadena)
- regex_fecha.sub(reemplazo, texto)

```python
# Base para cálculo relativo
fecha_base = datetime(2025, 5, 12)

def reemplazar_fecha(match):
    fecha_str = match.group(1) # Se explica en la siguiente subsección
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    delta = (fecha - fecha_base).days
    if delta == 0:
        return "CURRENT_DATE"
    elif delta > 0:
        return f"CURRENT_DATE + INTERVAL '{delta} days'"
    else:
        return f"CURRENT_DATE - INTERVAL '{abs(delta)} days'"

# Simulamos un texto con varias fechas que queremos sustituir
texto_sql = """
INSERT INTO stock_move (move_id, created_at, move_type, user_id)
VALUES (1, '2025-01-02', 'incoming', 1);

INSERT INTO stock_move_line (expiration_date)
VALUES ('2025-08-15');
"""
```

Aplicamos la transformación usando regex_fecha.sub() que funciona igual que re.sub(), pero con solo dos argumentos:

- `regex.sub(reemplazo, texto)`
  porque el patrón ya está incluido en el objeto compilado.

```python
texto_transformado = regex_fecha.sub(reemplazar_fecha, texto_sql) # Equivale a re.sub(r"'(\d{4}-\d{2}-\d{2})'", reemplazar_fecha, texto_sql)
print(texto_transformado)

# Salida:
# INSERT INTO stock_move (move_id, created_at, move_type, user_id)
# VALUES (1, CURRENT_DATE - INTERVAL '130 days', 'incoming', 1);
#
# INSERT INTO stock_move_line (expiration_date)
# VALUES (CURRENT_DATE + INTERVAL '95 days');
```

### Extraer coincidencias con `group()`

Cuando hacemos una búsqueda con re.search() o re.match(), el resultado es un objeto Match.
Podemos usar `group()` para extraer la parte del texto que coincide.

```python
texto = "La fecha del evento es '2025-07-17'"

# Coincidencia simple: todo el patrón
match = re.search(r"\d{4}-\d{2}-\d{2}", texto)
if match:
    print("group():", match.group())  # '2025-07-17'

# Coincidencia con paréntesis (grupo de captura)
match = re.search(r"'(\d{4}-\d{2}-\d{2})'", texto)
if match:
    print("group():", match.group())    # "'2025-07-17'" (todo el match)
    print("group(1):", match.group(1))  # "2025-07-17" (solo el grupo capturado entre paréntesis)

# group(0) es equivalente a group()
```

> `group()` devuelve el texto que coincide con **todo** el patrón.  
> `group(1)` devuelve el contenido del **primer grupo de captura** `(...)`.  
> `group(0)` es equivalente a `group()`.

---

### Resumen

- `match`, `search`, `findall`, `split` y `sub` cubren la mayoría de casos de uso.
- Usa **flags** como `re.I` para búsquedas “sin mayúsculas/minúsculas”.
- Valida formatos (emails, fechas…) con patrones y **anchors** `^`/`$`.
- Compila patrones con `re.compile` cuando vayas a reutilizarlos.
- Usa grupos de captura con `(...)` y recupéralos con `group(n)`.

> Las regex son potentes: empieza con patrones simples y añade complejidad poco a poco para mantener la legibilidad.

---

## Gestión de paquetes y módulos [🔝 Volver al inicio](#)

Python dispone de un **sistema de gestión de paquetes** muy completo llamado **PIP**,  
que permite instalar, actualizar y eliminar librerías externas fácilmente.  
Además, puedes crear tus propios **paquetes** para reutilizar código entre proyectos.

### PIP — Python Package Installer

PIP es la herramienta oficial para gestionar paquetes en Python y acceder a **PyPI**, el repositorio público de librerías [PyPI](https://pypi.org).

#### Instalación y comandos básicos

```python
# Verificar versión de PIP
pip --version
# En Windows: py -m pip --version

# Actualizar PIP
pip install --upgrade pip
# En Windows: py -m pip install --upgrade pip

# Instalar paquetes
pip install numpy
pip install pandas

# Listar paquetes instalados
pip list

# Mostrar información detallada de un paquete
pip show numpy

# Desinstalar un paquete
pip uninstall pandas
```

> 🔹 Los comandos de PIP funcionan igual en Linux, macOS y Windows,  
>  aunque en Windows suele precederse con `py -m`.  
> 🔹 PyPI (Python Package Index) aloja miles de librerías de código abierto.

### Ejemplo: uso de **NumPy**

NumPy es una de las librerías más populares de Python para **cálculo científico y manejo de arrays**.

```python
import numpy
print(numpy.version.version)
# Ejemplo: 1.26.4

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
# <class 'numpy.ndarray'>

print(numpy_array * 2)
# [ 70  48 124 104  60  60  34]
```

> 🔹 NumPy introduce su propio tipo de dato `ndarray` (N-dimensional array).  
> 🔹 Permite operar de forma vectorizada (sin bucles explícitos).  
> 🔹 Es la base de muchas otras librerías como **Pandas, Scikit-Learn o TensorFlow.**

### Ejemplo: uso de **Requests**

Requests es una librería HTTP sencilla y potente para **hacer peticiones web**.

```python
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
# <Response [200]>

print(response.status_code)
# 200

print(response.json())
# Devuelve un diccionario con el JSON de la API
```

> 🔹 `requests.get(url)` devuelve un objeto `Response`.  
> 🔹 Puedes acceder al contenido con `.text`, `.json()`, `.content` o `.status_code`.  
> 🔹 Ideal para consumir APIs REST o automatizar tareas web.

### Crear tu propio paquete

En Python, un **paquete** es una carpeta con módulos `.py` y un archivo `__init__.py` que indica a Python que esa carpeta debe tratarse como un paquete importable.

Ejemplo de estructura:

```python
mypackage/
├── __init__.py
└── arithmetics.py
```

Contenido de `arithmetics.py`:

```python
def sum_two_values(first_value, second_value):
    return first_value + second_value
```

> 🔹 El archivo `__init__.py` puede estar vacío, pero es necesario para reconocer la carpeta como paquete.  
> 🔹 Puedes organizar varios módulos dentro del mismo paquete.

### Importar un módulo o paquete propio

```python
from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))
# 5
```

> 🔹 Usa `from paquete import módulo` para importar desde tu propio código.  
> 🔹 Asegúrate de que el directorio raíz del proyecto esté en el **PYTHONPATH** o en el mismo nivel del script.

### Resumen

| Tarea                               | Herramienta / comando                     |
| ----------------------------------- | ----------------------------------------- |
| Instalar librería                   | `pip install nombre`                      |
| Desinstalar librería                | `pip uninstall nombre`                    |
| Listar paquetes                     | `pip list`                                |
| Mostrar información                 | `pip show nombre`                         |
| Crear paquete propio                | Carpeta con `__init__.py` y módulos `.py` |
| Instalar dependencias desde archivo | `pip install -r requirements.txt`         |

> En resumen:
>
> - **PIP** gestiona tus dependencias.
> - **PyPI** es el repositorio oficial de paquetes Python.
> - **Requests**, **NumPy**, **Pandas**, etc. son ejemplos de librerías externas.
> - Puedes crear y reutilizar tus propios **paquetes locales** o publicarlos en PyPI.

---

## Arrays en python [🔝 Volver al inicio](#)

Para trabajar con arrays en Python tenemos principalmente dos opciones: el módulo nativo `array` y la librería `numpy`. 

### ¿Cómo se usan?
#### A. El módulo array (Nativo)
Es parte de la librería estándar de Python. Se usa principalmente cuando necesitas ahorrar memoria pero no requieres hacer operaciones matemáticas complejas. Este tipo de array es unidimensional.
```python
import array

# Se debe especificar el tipo: 'i' para enteros, 'd' para decimales (float)
mi_array = array.array('i', [1, 2, 3, 4])
print(mi_array)
```
Los arrays son tipos de secuencias que se comportan de forma similar a las listas, a excepción que el tipo de objeto guardado debe definirse.

```python
# Añadir un elemento al final (in-place)
arr.append(5)
# Añadir varios elementos
arr.extend([6, 7])
print(arr)  # array('i', [1, 2, 3, 4, 5, 6, 7])
```
> [array — Arreglos eficientes de valores numéricos](https://docs.python.org/es/3.9/library/array.html)

#### B. NumPy Arrays (El estándar de la industria)
Es una librería externa. Es la opción preferida porque permite realizar operaciones matemáticas sobre todo el array sin usar bucles for. 
Permite múltiples dimensiones, es más rápido para cálculos matemáticos y requiere tipos de datos homogéneos.

```python
import numpy as np

# Se crean mucho más fácil y son ultra rápidos
np_array = np.array([1, 2, 3, 4])
print(np_array * 2)  # Resultado: [2, 4, 6, 8]
```

Añadir elementos (usando np.append) devuelve un nuevo array, no modifica el original, lo que puede ser lento en bucles:

```python
# Añadir elemento (devuelve un NUEVO array)
np_arr = np.append(np_arr, [5])
print(np_arr)  # [1 2 3 4 5]

# Para insertar en una posición específica
np_arr = np.insert(np_arr, 1, 99) # Insertar 99 en índice 1
print(np_arr)  # [ 1 99  2  3  4  5]
```

> [numpy.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

### Diferencias clave: Listas vs. Arrays
|Característica | Listas de Python | Arrays (array o numpy) |
| ------------- | -----------------| ---------------------- |
|Tipo de datos | Pueden mezclar todo (strings, ints, objetos).	| Homogéneos: Todos los elementos deben ser del mismo tipo.
|Memoria | Consumen mucha más memoria (almacenan punteros).	| Muy eficientes: Almacenan los datos de forma contigua.
|Rendimiento | Lentas para cálculos masivos.	| Ultra rápidos (especialmente NumPy) por su implementación en C.
|Funcionalidad | Métodos básicos (append, pop). | NumPy permite álgebra lineal, estadística y cálculos vectorizados.

### ¿Cuándo usar cada uno?
- Usa Listas si vas a guardar pocos elementos o si los datos son de diferentes tipos.
- Usa el módulo `array` si estás en un entorno con memoria muy limitada y solo necesitas una colección simple de números.
- Usa `NumPy` para cualquier cosa que involucre ciencia de datos, machine learning o si tienes que procesar miles de números eficientemente. 

## Retos de programación sencillos [🔝 Volver al inicio](#)

Cada reto está implementado en el archivo [`challenges.py`](../intermediate/challenges.py).  

---

## 🔗 Navegación

⬅️ [Lección anterior](./basic.md) | [Volver al índice principal](../README.md) | [Siguiente lección ➡️](./backend_fastapi.md)

---
