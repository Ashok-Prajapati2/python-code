import random

a = input("Enter name for list: ")
my_list = a.split()

len_mylist = len(my_list)
# print(len_mylist)


random_chouse = random.randrange(len_mylist-1)
print(f"Random choise is {my_list[random_chouse]}")
