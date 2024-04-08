string = "hello world"
print(string.capitalize())  #  Hello world

string = "HELLO WORLD"
print(string.lower())  #  hello world

string = "hello world"
print(string.upper())  #  HELLO WORLD

string = "hello world"
print(string.title())  #  Hello World

string = "Hello World"
print(string.swapcase())  #  hELLO wORLD

string = "Hello"
print(string.isalpha())  #  True

string = "Hello123"
print(string.isalnum())  #  True


string = "123"
print(string.isdigit())  #  True

string = "123"
print(string.isdecimal())  #  True

string = "   "
print(string.isspace())  #  True

string = "hello"
print(string.islower())  #  True

string = "HELLO"
print(string.isupper())  #  True

string = "Hello World"
print(string.istitle())  #  True

string = "   Hello, World!   "
print(string.strip())  #  Hello, World!


string = "Hello"
print(string.center(10, '*'))  #  **Hello***


string = "42"
print(string.zfill(5))  #  00042

string = "Hello World"
print(string.replace("World", "Python"))  #  Hello Python


string = "Hello World"
print(string.count("l"))  #  3

string = "Hello World"
print(string.find("World"))  #  6


string = "Hello World"
print(string.split())  #  ['Hello', 'World']


string = "Hello-World"
print(string.partition("-"))  #  ('Hello', '-', 'World')


words = ['Hello', 'World']
print(' '.join(words))  #  Hello World

name = "Ashok"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  #  My name is Ashok and I am 30 years old.
