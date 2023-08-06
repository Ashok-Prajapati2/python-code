import random

a = random.random()
print(a)


a = random.gauss(mu=100, sigma=50)
print(a)

a = random.betavariate(1, 1)
print(a)

mylist = ["apple", "banana", "cherry"]
a = random.choice(mylist)
print(a)

a = random.choices(mylist, weights=[1, 1, 10], k=5)
print(a)


a = random.gammavariate(100, 2)
print(a)


a = random.getrandbits(10)
print(a)


a = random.sample(range(9000000), k=5)
print(a)

# random.seed(10)
# print(random.random())

# random.seed(10)
# print(random.random())

a = random.randrange(1, 10)
print(a)

a = random.randint(5, 9)
print(a)
