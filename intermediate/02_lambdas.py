### Lambdas ###

# Funciones anónimas:
# Se crean con la palabra reservada "lambda" y se deben definir en una línea.
def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))

# Ideales para usar con map, filter, etc.

nums = [1, 2, 3]  
print(list(map(lambda x: x * 2, nums)))  
# [2, 4, 6]

print(list(filter(lambda x: x % 2 == 0, nums)))  
# [2]

print(sorted(["aa", "b", "ccc"], key=lambda s: len(s)))  
# ['b', 'aa', 'ccc']