# iterators 

for char in "python":
    print(char)

print("\n")

for i in {"a":5, "b":10}:
    print(i)

my_list = [1,2,3,4,5]

my_list1 = iter(my_list)

print(type(my_list1))

print(next(my_list1))
print(next(my_list1))
print(next(my_list1))
print(next(my_list1))
print(next(my_list1))
# print(next(my_list1))



