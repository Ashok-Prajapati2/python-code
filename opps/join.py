lis = ['a','b','c','d','g']

for i in lis:
    if i != 'g':
        print(i,'and',end=' ')
    else:
        print(i)

print()

print(" and ".join(lis))