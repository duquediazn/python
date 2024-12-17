#Usa snake_case:
my_string_variable = "My String variable"
my_int_variable = 5
my_bool_variable = False

print(my_string_variable) #My String variable
print(my_int_variable) #5
print(my_bool_variable) #False

#Concatenación de variables en un print
print(my_bool_variable, my_int_variable, my_string_variable) #False 5 My String variable
print(type(print(my_bool_variable, my_int_variable, my_string_variable))) #<class 'NoneType'>

print(type(str(my_int_variable))) #<class 'str'>
