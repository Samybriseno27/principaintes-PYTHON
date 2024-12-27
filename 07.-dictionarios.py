### Dictionario ###

my_dict = dict()
my_other_dict ={}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict ={"Nombre:""sam","apellido","briseño","edad",28, "1:python"}
print(my_other_dict)

my_dict= {
    "Nombre": "sam",
    "apellido": "briseño",
    "edad" : 28,
    "lenguajes" :{"python,","swift","kotlin"},
    1:1.177
    
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict)
print(my_dict["Nombre"])

my_dict ["Nombre"] = "sam"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["calle"] = "calle sam"
print(my_dict)

del my_dict ["calle"]
print(my_dict)

print("sam" in my_dict)
print("apellid" in my_dict)

print(my_dict.item())
print(my_dict.key())
print(my_dict.value())