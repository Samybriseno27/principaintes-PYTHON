### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,1.77,"sam","briseño","sam")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple)[4] indexerror
#print(my_tuple)[-6] indexerror

print(my_tuple.count("sam"))
print(my_tuple.index("briseño"))


#my_tuple [1]= 1.80 "tuple" objet does not support item assignment

my_sun_tuple = my_tuple + my_other_tuple
print(my_sun_tuple)


print(my_sun_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))