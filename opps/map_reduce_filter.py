# map function 

list1 = [1,2,3,4]

# sq = []
# for i in list1:
#     sq.append(i**2)

def square(a):
    return a**2

sq = list(map(square,list1))
print(sq)


# filter function
def grater(n):
    if n>=5:
        return True
    else:
        return False
list2 = [2,4,58,2,5,5,82,3,2,1,2]

list3 = list(filter(grater,list2))
print(list3)


# reduce function

from functools import reduce

def sum_num(a,b):
    return a+b+2

ans =  reduce(sum_num,[1,2,52,5,25,5])
print(ans)
