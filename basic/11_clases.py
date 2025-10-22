### Classes ###
# https://docs.python.org/es/3/tutorial/classes.html

# Definición

class MyEmptyPerson: #Por convención, los nombres de las clases se escriben en PascalCase.
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
# En Python, los atributos se definen directamente en el constructor o incluso fuera de él. 
# A diferencia de otros lenguajes, no necesitas declararlos explícitamente al inicio.

# Encapsulamiento:
# Los atributos o métodos públicos se definen normalmente.
# Los protegidos se prefijan con _ (convención, no es estrictamente privado).
# Los privados se prefijan con __ (esto aplica 'name mangling' para evitar colisiones de nombres).
    def __init__(self, name, surname, alias="Sin alias"): # Constructor
        #self.name = name
        #self.surname = surname
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública, 'self' es el equivalente a 'this'
        self.__name = name  # Propiedad privada
# Los métodos se definen como funciones dentro de una clase y siempre reciben self como primer parámetro.
    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Nazaret", "Duque")
#print(my_person.name)
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

# Métodos estáticos: 
class Utilidad:
    @staticmethod #opcional
    def sumar(a, b):
        return a + b

resultado = Utilidad.sumar(5, 10)
print(resultado)  # 15

# Atributos estáticos: 
class Configuracion:
    version = "1.0.0"  

print(Configuracion.version)  # 1.0.0
Configuracion.version = "1.1.0"
print(Configuracion.version)  # 1.1.0

#Acceso desde una instancia:
config1 = Configuracion()
config2 = Configuracion()
print(config1.version)  # 1.1.0
print(config2.version)  # 1.1.0


# Métodos de Clase
# Aunque no son estrictamente "estáticos", los métodos de clase (@classmethod) son una alternativa interesante. 
# Usan cls como referencia y permiten trabajar con atributos estáticos de la clase.
class Configuracion:
    version = "1.0.0"

    @classmethod
    def obtener_version(cls):
        return cls.version

print(Configuracion.obtener_version())  # 1.0.0

#Ejemplo de uso completo (métodos de la clase y métodos y atributos estáticos):
class Banco:
    tasa_interes = 0.05  # Atributo estático

    def __init__(self, saldo):
        self.saldo = saldo  # Atributo de instancia

    def calcular_interes(self):
        return self.saldo * Banco.tasa_interes

    @staticmethod
    def info_bancaria():
        return "Este es el Banco ABC."

    @classmethod
    def actualizar_tasa_interes(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa

# Uso de atributos y métodos
print(Banco.info_bancaria())  # Este es el Banco ABC.

cliente = Banco(1000)
print(cliente.calcular_interes())  # 50.0

Banco.actualizar_tasa_interes(0.06)
print(cliente.calcular_interes())  # 60.0

# Polimorfismo:
# Python soporta polimorfismo dinámico (sobrescritura de métodos) sin necesidad de usar anotaciones explícitas

class Vehiculo:
    def avanzar(self):
        return "El vehículo avanza"

class Bicicleta(Vehiculo):
    def avanzar(self):
        return "La bicicleta avanza pedaleando"

vehiculos = [Vehiculo(), Bicicleta()]

for v in vehiculos:
    print(v.avanzar())

# Atributos dinámicos:
# Puedes añadir atributos a los objetos de forma dinámica.
p = Person("Pedro", "Hdez")
p.edad = 36
print(p.edad)

# Herencia:

class AnotherPerson(Person):
     def caminar(self):
        #Puedes usar super() para acceder a los métodos de la clase base
        return super().walk()

persona = AnotherPerson("Nazaret", "Duque")
print(persona.caminar())

# En Python Existe herencia múltiple:
# Python utiliza un mecanismo llamado C3 Linearization 
# (o MRO, Method Resolution Order) para manejar los posibles conflictos en la herencia múltiple

class ClaseBase1:
    def metodo_base1(self):
        return "Método de ClaseBase1"

class ClaseBase2:
    def metodo_base2(self):
        return "Método de ClaseBase2"

class ClaseDerivada(ClaseBase1, ClaseBase2):
    pass

# Crear una instancia de ClaseDerivada
obj = ClaseDerivada()
print(obj.metodo_base1())  # Método de ClaseBase1
print(obj.metodo_base2())  # Método de ClaseBase2

# Orden de resolución de métodos (MRO)
# Cuando hay herencia múltiple, Python sigue un orden específico para buscar métodos y atributos. 
# Este orden es determinado por el algoritmo C3 Linearization y puede consultarse con el atributo 
# especial .__mro__ o usando help().

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
print(D.__mro__)    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Python busca el método saludar en el orden: D -> B -> C -> A -> object.

# Ejemplo Práctico con super():
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

#Salida: 
# Acción en A
# Acción en C
# Acción en B
# Acción en D