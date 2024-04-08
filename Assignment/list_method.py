my_list = [1, 2, 3]


my_list.append(4)
print("After appending 4:", my_list)  #  [1, 2, 3, 4]


my_list.extend([5, 6])
print("After extending with [5, 6]:", my_list)  #  [1, 2, 3, 4, 5, 6]

my_list.insert(2, 10)
print("After inserting 10 at index 2:", my_list)  #  [1, 2, 10, 3, 4, 5, 6]

my_list.remove(3)
print("After removing 3:", my_list)  #  [1, 2, 10, 4, 5, 6]

popped_item = my_list.pop()
print("Popped item:", popped_item)  #  6
print("List after popping:", my_list)  #  [1, 2, 10, 4, 5]


my_list.clear()
print("List after clear():", my_list)  #  []

my_list = [1, 2, 3, 4, 5]

print("Index of 3:", my_list.index(3))  #  2


print("Count of 3:", my_list.count(3))  #  1

my_list.sort()
print("Sorted list:", my_list)  #  [1, 2, 3, 4, 5]


my_list.reverse()
print("Reversed list:", my_list)  #  [5, 4, 3, 2, 1]


new_list = my_list.copy()
print("Copied list:", new_list)  #  [5, 4, 3, 2, 1]

print("Length of the list:", len(my_list))  #  5


print("Minimum value in the list:", min(my_list))  #  1

print("Maximum value in the list:", max(my_list))  #  5


print("Sum of the list elements:", sum(my_list))  #  15


print("Any element in the list:", any(my_list))  #  True


print("All elements in the list:", all(my_list))  #  True

print("Sorted list:", sorted(my_list))  #  [1, 2, 3, 4, 5]

print("Slice of first three elements:", my_list[:3])  #  [5, 4, 3]
