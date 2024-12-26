### Modules ###

from math import pi as PI_VALUE #Así importamos solo lo que queremos del módulo
import math #Así importamos todo el módulo
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)  #Si importamos todo el módulo accedemos así
my_module.printValue("Hola Python!")


sumValue(5, 3, 1) #Si importamos las funciones concretas podemos acceder solo con el nombre de la función
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)