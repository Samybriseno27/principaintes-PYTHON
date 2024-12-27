### Strings ###

my_string ="mi string"
my_other_string = "Mi  otro string"

print(len(my_string))  # Longitud de my_string
print(len(my_other_string))  # Longitud de my_string

print(my_string + my_other_string)

my_new_line_string = "este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "este es un string\tcon tabulación"
print(my_tab_string)

my_tab_string = "este es un string\tcon tabulación"
print(my_tab_string)

#fORMATEO

name,surname,age ="sam","briseño" , 28
print("Mi nombre es {} y mi edad es {}".format(name, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es {name} {surname} y mi edad es {age}")

#desempaqueando de caracter

# Desempaquetando caracteres
languaje ="python"
a, b,c,d,e,f = languaje
print(a)  # b
print(e)  # p

#division

languaje_slice =languaje[1:3]
print(languaje_slice)

languaje_sli =languaje[1:]
print(languaje_slice)

#reverse
reversed_languaje = languaje[::-1]

#funciones
print(languaje.capitalize())  # Capitalize the first letter
print(languaje.upper())       # Convert to uppercase
print(languaje.lower())       # Convert to lowercase
print(languaje.count('t'))    # Count occurrences of 't'
print(languaje.find('o'))     # Find the position of 'o'
