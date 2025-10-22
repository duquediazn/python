### Regular Expressions ###

from datetime import datetime
import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) # Con match() comprobamos si coinciden desde el principio (y hasta donde). re.I es un flag para ignorar el casing
print(match) # <re.Match object; span=(0, 18), match='Esta es la lección'>
start, end = match.span() # match.span() -> (0,18)
print(my_string[start:end]) # Esta es la lección

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string)) # None. Porque no coinciden desde el principio.

# search

search = re.search("lección", my_string, re.I) # Como el match, pero no tiene que ser desde el principio
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I) # Encuentra todas las coincidencias y las devuelve en una lista
print(findall)

# split

print(re.split(":", my_string)) # Nos hace un split con el separador como primer argumento. Devuelve una lista.

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string)) # Sustituye lección o Lección por LECCIÓN
print(re.sub("Expresiones Regulares", "RegEx", my_string))


### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string)) 

pattern = r"\D"
print(re.findall(pattern, my_string))  

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))


### Usar re.compile(): ejemplo aplicado a fechas ###

# A veces es útil compilar una expresión regular para reutilizarla varias veces de forma eficiente
# El método re.compile(patrón) permite "precompilar" una expresión regular.
# Esto crea un objeto de tipo re.Pattern que se puede reutilizar, lo cual mejora la legibilidad y eficiencia si vas a usar la expresión varias veces.

# Por ejemplo:

# Queremos encontrar fechas tipo '2025-01-02' dentro de un texto
regex_fecha = re.compile(r"'(\d{4}-\d{2}-\d{2})'")
print(type(regex_fecha)) # <class 're.Pattern'>
print(regex_fecha) # re.compile("'(\\d{4}-\\d{2}-\\d{2})'")

# Una vez compilada, puedes usar métodos como:
# - regex_fecha.match(cadena)
# - regex_fecha.search(cadena)
# - regex_fecha.findall(cadena)
# - regex_fecha.sub(reemplazo, texto)

# Usamos una fecha base para calcular el desplazamiento relativo
fecha_base = datetime(2025, 5, 12)

# Función que calcula el intervalo relativo y devuelve CURRENT_DATE +/- INTERVAL 'X days'
def reemplazar_fecha(match):
    fecha_str = match.group(1) # para extraer la fecha sin las comillas simples (group() se explica más abajo)
    fecha = datetime.strptime(fecha_str, "%Y-%m-%d") # con strptime() creamos un nuevo objeto datetime "parseado" desde un string
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

# Aplicamos la transformación usando regex_fecha.sub() que funciona igual que re.sub(), pero con solo dos argumentos:
#   regex.sub(reemplazo, texto)
# porque el patrón ya está incluido en el objeto compilado.
texto_transformado = regex_fecha.sub(reemplazar_fecha, texto_sql) # Equivale a re.sub(r"'(\d{4}-\d{2}-\d{2})'", reemplazar_fecha, texto_sql)
print(texto_transformado)


### Usar group() para extraer coincidencias ###

# Cuando hacemos una búsqueda con re.search() o re.match(), el resultado es un objeto Match.
# Podemos usar .group() para extraer la parte del texto que coincide.

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
