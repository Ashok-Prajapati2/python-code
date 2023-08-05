import random 
import second


print(second.pi)
a = random.random()
print(a)


a = random.gauss(mu = 100, sigma =50)
print(a)

a = random.betavariate(1,1)
print(a)

mylist = ["apple", "banana", "cherry"]
a = random.choice(mylist)
print(a)