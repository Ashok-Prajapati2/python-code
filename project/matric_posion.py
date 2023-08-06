#        1     2     3

lis1 = [" ", " ", " "]
lis2 = [" ", " ", " "]
lis3 = [" ", " ", " "]

map = [lis1, lis2, lis3]
print(map)
print(f" {lis1}\n {lis2} \n {lis3}")

set_position = input("enter position: ")
value = input("Enter value for this index: ")
horizontal = int(set_position[0])
vertical = int(set_position[1])

set_row = map[vertical-1]
set_col = set_row[horizontal-1]
set_row[horizontal-1] = value

print(f" {lis1}\n {lis2} \n {lis3}")
