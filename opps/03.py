# genrator 


def gen(n):
    for i in range(n):
        yield i
# for i in range(1000000):
    # print(i)

print(gen(100000))

for i in gen(100000):
    print(i)
obj1 = gen(5)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
# print(next(obj1)) # error  StopIteration


num = 123 

# for i in num:
    # print(i) # TypeError: 'int' object is not iterable
    

num = "python"
for i in num:
    print(i) # 'str' object is  iterable
    