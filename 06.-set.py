### set ###

my_Set = set()
my_other_set = {}

print(type(my_Set))
print(type(my_other_set)) #inicialmente es un dicionario 

my_other_set ={"sam,""briseño",28}
print(type(my_other_set))

print(len(my_other_set))
 
print(my_other_set) # es un set no es una estructura de datos ordenadas
my_other_set.add("sam") #un set no admite repetid


print(my_other_set)

print("sam" in my_other_set)
print("sam" in my_other_set)

my_other_set.remove("sam")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_Set) Nameerror name "my_other_set" is not definded

my_set = {"sam","briseño",28}
my_list =list(my_set)
print(my_list)  

my_other_list = {"Kotlin","Swift","python"}

# Corrected union operation
print(my_set.union({"kotlin", "C#"}))

# Corrected difference operation
print(my_set.difference(my_other_list))



