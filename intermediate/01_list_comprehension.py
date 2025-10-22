### List Comprehension ###

# Python nos permite modificar colecciones iterables en una sola línea de código

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

# Definición
# Python nos permite hacer:
my_list = [i + 1 for i in range(8)]
print(my_list)

# En lugar de hacer: 
my_other_list = []
for i in range(8):
    my_other_list.append(i+1)
print(my_other_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)