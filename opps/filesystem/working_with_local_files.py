file = open('/home/ashok/Desktop/python-code/opps/filesystem/my_file.txt')
contents = file.read()
print(contents)
file.close()

file = open('/home/ashok/Desktop/python-code/opps/filesystem/my_file.txt', mode = 'r' )
contents = file.read()
print(contents)
file.close()

file = open('/home/ashok/Desktop/python-code/opps/filesystem/my_file.txt', mode = 'w' )
contents = file.write("Hello")
print(contents) ##this is not readable
file.close()

with open('/home/ashok/Desktop/python-code/opps/filesystem/my_file.txt', mode = 'a' ) as file:
    file.write(", Ashok")
    
   
with open('/home/ashok/Desktop/python-code/opps/filesystem/name.txt') as name_file:
    names = name_file.readlines()
    names = [name.strip() for name in names]  # Remove newline characters and store names in a list
    print(names)
    
with open('/home/ashok/Desktop/python-code/opps/filesystem/latter.txt' ) as w_file:
   letter_content = w_file.read()
   print(letter_content)
   
# Replace placeholder with each name and print the updated letter
for name in names:
    new_letter = letter_content.replace('name', name)
    print(new_letter)
    with open(f'/home/ashok/Desktop/python-code/opps/filesystem/new_{name}.txt',mode="w" ) as com_Latter:
        com_Latter.write(new_letter)
        



# ----------------------------------------------------------------
txt = '    banana    '
print(txt)
print(txt.strip())    
# ----------------------------------------------------------------

