dic = {"key":"value"}
print(dic)
print(dic['key'])

# adding new items to dic

dic['new_key'] = 'new_value'

print(dic)

# change value
dic['key'] = 'change_value'

print(dic)

empty_dic = {}

for n in range(10):
    empty_dic[n] = n+1
    
print(empty_dic)

for n in empty_dic:
    print(n , empty_dic[n])
    