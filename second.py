
# list file

list_is = ['item1','item2',5326 ,53]
print(list_is)

list_is.append("item append")
print(list_is)

   
list_is[1] = 'item change'
print(list_is)

list_is.extend("Ashok")
print(list_is)


for item in list_is:
    print(item)


name_is = input("Enter name of your friend: ")

my_list = name_is.split()

print(my_list)


