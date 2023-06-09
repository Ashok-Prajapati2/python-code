#Hi , it is python code
# print() function
print("Hellow world!")
print("Hellow" + " " + "ASHOK")


# input() function

a = input("What is your name?\n")
print("\n" + a)

#len() function
b = len(a)
print(b)

#python variables

name = input("what is your name? \n")
print(name)

a = input("please enter first number a: ")
b = input("please enter second number b: ")

# a=b , b=c

c = a
a = b
b = c
ans = f"a:{a} \n b:{b}"
print(ans)

#len()
# print(len(123)) #this is type error
a = 123
b = str(a)
print(len(b))

#substring
print("Hellow"[0])


a = 123_456_789
print(a) # for easy 

# type () function // data types
a = 123
b = 12.5
c = True
d = "ASHOK"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# input 2 digit number ex = 23 , and add = 5 

a = input("please enter two digit number : ")
b = int(a[0])
c = int(a[1])
result = b+c
print(f"\n {result}")


#operaters

print(4+5 , 5-4 , 5*4 , 6//2 , 2**2)
print(6/3) # float value

#round() function for float value 
print(round(89/15 , 2))

# age to days caculate
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age  = input("Enter your age: ")
int_age = int(age)
year = 90 - int_age
days = year*365
weeks = year * 52
month = year * 12

result = f"year {year}, days{days},weeks {weeks},month {month}"
print(result)

# bill split in between some people

a = float(input("Enter total bill : "))
b = int(input("how many people to split the bill ? : "))
c = float(input("Enter tip : "))

result = (a+c)/b
print(result)

