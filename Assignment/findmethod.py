####  find char into a  string ###

s = "This is a string to find char T"
s = s.lower()


# using loop to find 't' index
char_list_0 = []

i = 0
for char in s:
    if char == 't':
        char_list_0.append(i)
    i += 1

print("using loop",char_list_0)

# using  slicing. to find 't' index

char_list_1 = []

start_index = 0

while True:

    index = s.find('t', start_index)

    # string.find(value, start, end) 

    # print(index)

    if index == -1:
        break
    char_list_1.append(index)
    start_index = index + 1

print("using  slicing",char_list_1)

# List comprehension  to find 't' index
print("List comprehension", [i for i, char in enumerate(s, 0) if char == 't'])

# using other method to loop 

print("using other method to loop ", [i for i in range(len(s)) if s[i] == 't'])

