#Variables

my_string_variable = "MY string Variable"
print (my_string_variable)

my_int_variable = 5
print (my_int_variable)

my_int_to_Str_variable = str(my_int_variable)
print(my_int_to_Str_variable)
print(type(my_int_to_Str_variable))

my_bool_variable =False
print(my_bool_variable)

#concatanacion de variablese en un print
print(my_string_variable,str(my_int_to_Str_variable),my_bool_variable)
print("este es el valor de",my_bool_variable)


# algunas funciones del sistema funciones del sistema
print(len(my_string_variable))

# variables en una sola linea

name, surname, alias, age = "sam", "briseño", "samy", 28
print("Me llamo:", name, surname, "Mi edad es:", age, "y mi alias es:", alias)

#inputs

first_name =input("cual es tu nombre")
age =input ("cual es tu edad")

print(first_name)
print(age)

#cambio su tipo
name = sam
age ="briseño"
print(name)
print(age)

#funciones el tipo
address: str ="mi direccion"
adrees = 28
print(adrees)
address = True
address = 5
address = 1.2
