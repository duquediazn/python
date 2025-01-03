### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0 :
            print("fizzbuzz")    
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)
            
#fizz_buzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
'''
def is_anagram(palabra1 : str, palabra2 : str): 
    if palabra1.lower() == palabra2.lower() or len(palabra1) != len(palabra2):
        return False
    for i in palabra1.lower():
        if palabra2.lower().count(i) < 1:
            return False
    return True

print(is_anagram("Army", "Mary"))
'''
#Moure:
def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


#print(is_anagram("Amor", "Roma"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    fib_0 = 0
    fib_1 = 1

    for i in range(50):
        print(fib_0)
        fib_n = fib_0 + fib_1
        fib_0=fib_1
        fib_1=fib_n    

#fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


def is_prime(n):
    if n >= 2:
        for i in range(3,n):
            if n%i == 0:
                return False
        return True
    return False

def print_primes_between(ini, fin):
    for i in range(ini, fin):
        if is_prime(i):
            print(i)



'''
#Moure:
def is_prime():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break

            if not is_divisible:
                print(number)

'''

#print_primes_between(1, 101)

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text: str):
    reversed=""
    for i in text:
        reversed=i+reversed
    return reversed


'''
#Moure:

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text
'''

#print(reverse("Hola mundo"))