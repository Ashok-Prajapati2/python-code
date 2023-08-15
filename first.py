

# hi , i'm Ashok , I start advance python.

print("Hellow World !")

# basic of bython

print("print func use for print any data")

# operators + - *  / ** %

print(5+5, 5-6, 5*6, 10/2, 10//2, 10 % 3, 2**3)

# data types

a = 12
print(type(a))

a = 12.0
print(type(a))

a = 'ASHOK'

print(type(a))


# user input

nam = input("Enter any inpput: ")
print(type(nam))
print(nam)

a = '1252'
b = int(a)
print(type(b), b)

# other operaters  < > <= >= !=

# conditinal Execuation

a = 10
if a < 5:
    print("a lessthen five")

if a > 5:
    print("a graterthen five")


# python data types

# int = 12
# float = 20.0
# str = "ashok"
# list = [10, 'ashok', 10.2]
# tuple = (10, 'ashok', 10.2)
#  bool = True % False
# set = ("A", "B")
# dict = {"key1": "value1", "key2": "value2", "key3": "value3"}


# loops
x = 0
while x < 5:
    x += 1
    print(x, "ASHOK")

    if x == 2:
        break

for x in range(1, 10, 2):
    print(x)



def out(x):
    return x

a = 10
b = 'blue'

class Bird:
    def __init__(self , a , b):
        hight = self.a
        color = self.b

    def bird_prop(hight,color):
        print(hight , color)
    
 

print(Bird.bird_prop(a,b))

