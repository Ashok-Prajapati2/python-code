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
print(string.isnumeric())  #  True

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

string = "   Hello, World!   "
print(string.lstrip())  #  Hello, World!

string = "   Hello, World!   "
print(string.rstrip())  #     Hello, World!

string = "Hello"
print(string.center(10, '*'))  #  **Hello***

string = "Hello"
print(string.ljust(10, '*'))  #  Hello*****

string = "Hello"
print(string.rjust(10, '*'))  #  *****Hello

string = "42"
print(string.zfill(5))  #  00042

string = "Hello World"
print(string.replace("World", "Python"))  #  Hello Python

string = "Hello\tWorld"
print(string.expandtabs())  #  Hello   World

string = "Hello World"
print(string.count("l"))  #  3

string = "Hello World"
print(string.find("World"))  #  6

string = "Hello World"
print(string.rfind("o"))  #  7

string = "Hello World"
print(string.index("World"))  #  6

string = "Hello World"
print(string.rindex("o"))  #  7

string = "Hello World"
print(string.startswith("Hello"))  #  True

string = "Hello World"
print(string.endswith("World"))  #  True

string = "Hello World"
print(string.split())  #  ['Hello', 'World']

string = "Hello World"
print(string.rsplit())  #  ['Hello', 'World']

string = "Hello-World"
print(string.partition("-"))  #  ('Hello', '-', 'World')

string = "Hello-World"
print(string.rpartition("-"))  #  ('Hello', '-', 'World')

words = ['Hello', 'World']
print(' '.join(words))  #  Hello World

string = "Hello World"
print(string.encode(encoding='utf-8'))  #  b'Hello World'

string = b'Hello World'
print(string.decode(encoding='utf-8'))  #  Hello World

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  #  My name is Alice and I am 30 years old.
