### Dates ###

from datetime import timedelta, date, time, datetime, timezone

# Datetime (fecha y hora)

now = datetime.now() 

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp()) # Representación única de una fecha.


print_date(now)

year_2023 = datetime(2023, 1, 1) # Mínimo tres parámetros (año, mes, día)

print_date(year_2023)

# Time (horas)
 
current_time = time(21, 6, 0) 

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date (fechas)

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas (tienen que ser objetos del mismo tipo)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# Timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

print(datetime.now()) # Naive (sin zona horaria), depende de la configuración de zona horaria del sistema donde se ejecuta.
print(datetime.now(timezone.utc)) # Aware (con zona horaria), no depende de la zona horaria del sistema, siempre es UTC.