print("Greatest out of three")

a = int(input("Enter first number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))

if a == b == c:
    print("All numbers are equal")

elif a >= b and a >= c:
    print(a, " is greatest") 

elif b >= a and b >= c:
    print(b, " is greatest") 

else:
    print(c, " is greatest") 

