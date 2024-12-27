### List ###

my_list = list()
my_other_list = []

print(len(my_other_list))

my_list = [35,24,62,52,52,30,17]
print(my_list)
print(len(my_list))

my_other_list = [35,1.77, "sam" ,"briseño"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])


my_other_list.append("sam")
print(my_other_list)

my_other_list.insert(1,"azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_list.clear()
print(my_list)

my_list ="hola python"
print(my_list)
print(type(my_list))