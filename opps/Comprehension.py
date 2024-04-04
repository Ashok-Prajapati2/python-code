# list Comprehension

list2 = [i for i in range(100) if i % 5 == 0]

print(list2)

# Dictinary Comprehension
# {key: value for element in iterable}

print({x:x**2 for x in range(10)})

dic = {
    'a':2,
    'b':5,
    'A':5,
}

dic2 = { k.lower(): dic.get(k.lower(),0)+ dic.get(k.upper(),0) for k in dic.keys()}
print(dic2)


# set comprehension

set1 = {i**2 for i in [1,2,5,2,4,5,2,4,2,4,2,5,2,412,2,2]}
print(set1)