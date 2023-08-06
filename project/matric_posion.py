#        1     2     3

lis1 = ["1", "4", "5"]
lis2 = ["2", "6", "7"]
lis3 = ["3", "8", "9"]

map = [lis1, lis2, lis3]
print(map)
print(f" {lis1}\n {lis2} \n {lis3}")

set_position = input("enter position: ")
value = input("Enter value for this index: ")
horizontal = int(set_position[0])
vertical = int(set_position[1])

set_row = map[horizontal-1]
# print(set_row)
set_col = set_row[vertical-1]
# print(set_col)
set_row[vertical-1] = value
# print(set_row[horizontal-1])
print(f" {lis1}\n {lis2} \n {lis3}")
