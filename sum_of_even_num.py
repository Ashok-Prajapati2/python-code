total = 0

for n in range(0 , 101 , 2):
    total += n
print(total)

total = 0
for n in range(0,101):
    if n%2 == 0:
        total += n
print(total)        