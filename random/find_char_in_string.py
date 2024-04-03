

def find_using_loop(s, char):
    char_list = []
    i = 0
    for ch in s:
        if ch == char:
            char_list.append(i)
        i += 1
    return char_list


def find_using_slicing(s, char):
    char_list = []
    start_index = 0
    while True:
        index = s.find(char, start_index)
        if index == -1:
            break
        char_list.append(index)
        start_index = index + 1
    return char_list


def find_using_list_comprehension(s, char):
    return [i for i, ch in enumerate(s) if ch == char]


def find_using_other_method(s, char):
    return [i for i in range(len(s)) if s[i] == char]


s = "This is a string to find char T"
s = s.lower()
char = 't'

print("Using loop:", find_using_loop(s, char))
print("Using slicing:", find_using_slicing(s, char))
print("List comprehension:", find_using_list_comprehension(s, char))
print("Using other method to loop:", find_using_other_method(s, char))
